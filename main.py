import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QAction, QMenu
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from box import *
from tablet import *

def openSecondWindow():
	window.close()
	window2.show()
	window2.rolled_sheet.show()

if __name__ == '__main__':
	app=QApplication(sys.argv)
	window=Box()
	window.show()	
	window.destroyed.connect(openSecondWindow)
	window2=Tablet()
	sys.exit(app.exec_())