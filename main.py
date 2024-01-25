import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QAction, QMenu
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from box import *
from tablet import *
from settings import SettingsWindow

def openSecondWindow():
	window.close()
	window2.show()
	window2.rolled_sheet.show()

if __name__ == '__main__':
	if os.path.exists("conf"):
		try:
			app=QApplication(sys.argv)
			window=Box()
			window.show()	
			window2=Tablet()
			window.destroyed.connect(openSecondWindow)
		except Exception as err:
			window.destroy()
			setup_window=SettingsWindow()
			setup_window.show()
			print(err)
	else:
		app = QApplication(sys.argv)
		setup_window=SettingsWindow()
		setup_window.show()
	sys.exit(app.exec_())