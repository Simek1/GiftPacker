import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QAction, QMenu
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from tablet import *

class Box(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.box=QPixmap("imgs/closedbox.png")
		self.scissors=QPixmap("imgs/scissors.png")

		desktop=QApplication.desktop()
		screen_geometry=desktop.screenGeometry()
		self.screen_width=screen_geometry.width()
		screen_height=screen_geometry.height()


		self.label = QLabel(self)
		if self.screen_width<1920:
			self.scalar=self.screen_width/1920
			self.box=self.box.scaled(int(self.box.width()*self.scalar), int(self.box.height()*self.scalar))
			self.scissors=self.scissors.scaled(int(self.scissors.width()*self.scalar), int(self.scissors.height()*self.scalar))
		self.label.setPixmap(self.box)
		self.label.setGeometry(0, 0, self.box.width(), self.box.height())
		self.setGeometry(int(self.screen_width/2)-int(self.box.width()/2), 0, self.box.width(), self.box.height())


		self.second_window=SecondWindow(self.scissors, self.screen_width, screen_height)

		self.collision_timer=QTimer(self)
		self.collision_timer.timeout.connect(self.check_collision)
		self.collision_timer.start(100) 

		self.animation_path=["imgs/openingbox.png",
					   "imgs/openingbox2.png",
					   "imgs/openingbox3.png",
					   "imgs/openingbox4.png"]
		self.animation_index=-1
		self.animation_timer=QTimer(self)
		self.animation_timer.timeout.connect(self.next_image)

	def check_collision(self):
		x, y=self.second_window.pos().x(), self.second_window.pos().y()
		if self.pos().x()<=x<=self.pos().x()+self.size().width() \
				and self.pos().y()<=y<=self.pos().y()+self.size().height():
			del(self.second_window)
			self.animation_index=0
			self.collision_timer.stop()
			self.animation_timer.start(1000)
		else:
			self.second_window.show()
	
	
	def contextMenuEvent(self, event):
		menu = QMenu(self)
		close_action = menu.addAction("Exit")
		action = menu.exec_(self.mapToGlobal(event.pos()))

		if action == close_action:
			sys.exit()
	
	def next_image(self):
		if self.animation_index<4:
			self.box=QPixmap(self.animation_path[self.animation_index])
			if self.screen_width<1920:
				self.box=self.box.scaled(int(self.box.width()*self.scalar), int(self.box.height()*self.scalar))
			self.label.setPixmap(self.box)
			self.animation_index+=1
		else:
			self.animation_timer.stop()
			self.destroyed.emit()

class SecondWindow(QWidget):
	def __init__(self, pixmap, width, height):
		super().__init__()
		self.pixmap=pixmap
		self.screen_width=width
		self.screen_height=height
		self.initUI()

	def initUI(self):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.label = QLabel(self)
		self.label.setGeometry(0, 0, self.pixmap.width(), self.pixmap.height())
		self.label.setPixmap(self.pixmap)
		self.setGeometry(self.screen_width-15,int(self.screen_height/2), self.pixmap.width(), self.pixmap.height())

	def mousePressEvent(self, event):
		if event.button()==Qt.LeftButton:
			self.offset=event.pos()

	def mouseMoveEvent(self, event):
		if event.buttons()==Qt.LeftButton:
			self.move(event.globalPos() - self.offset)
