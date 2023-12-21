import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QAction, QMenu
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.box=QPixmap("imgs/closedbox.png")
		self.scissors= QPixmap("imgs/scissors.png")


		label = QLabel(self)
		label.setPixmap(self.box)
		label.setGeometry(0, 0, self.box.width(), self.box.height())
		self.setGeometry(0,0, self.box.width(), self.box.height())

		self.second_window=SecondWindow(self.scissors)

		self.collision_timer = QTimer(self)
		self.collision_timer.timeout.connect(self.check_collision)
		self.collision_timer.start(100) 

	def check_collision(self):
		x, y = self.second_window.pos().x(), self.second_window.pos().y()
		if self.pos().x() <= x <= self.pos().x() + self.size().width() \
				and self.pos().y() <= y <= self.pos().y() + self.size().height():
			self.second_window.hide()
		else:
			self.second_window.show()
	
	
	def contextMenuEvent(self, event):
		menu = QMenu(self)
		close_action = menu.addAction("Exit")
		action = menu.exec_(self.mapToGlobal(event.pos()))

		if action == close_action:
			sys.exit()

class SecondWindow(QWidget):
	def __init__(self, pixmap):
		super().__init__()
		self.pixmap=pixmap
		self.initUI()

	def initUI(self):
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.label = QLabel(self)
		self.label.setGeometry(0, 0, self.pixmap.width(), self.pixmap.height())
		self.label.setPixmap(self.pixmap)
		self.setGeometry(1400, 300, self.pixmap.width(), self.pixmap.height())

	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.offset = event.pos()

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(event.globalPos() - self.offset)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())