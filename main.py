import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QAction, QMenu
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.box=QPixmap("imgs/closedbox.png")

		label = QLabel(self)
		label.setPixmap(self.box)
		label.setGeometry(0, 0, self.box.width(), self.box.height())
		self.setGeometry(0,0, self.box.width(), self.box.height())

	
	
	def contextMenuEvent(self, event):
		menu = QMenu(self)
		close_action = menu.addAction("Exit")
		action = menu.exec_(self.mapToGlobal(event.pos()))

		if action == close_action:
			sys.exit()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())