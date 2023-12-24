import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QAction, QMenu
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class Tablet(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.tabletoff=QPixmap("imgs/tabletoff.png")
		self.tableton=QPixmap("imgs/tableton.png")
		self.tabletcam=QPixmap("imgs/tabletcam.png")
		self.tabletquiz=QPixmap("imgs/tabletquiz.png")
		self.tabletback=QPixmap("imgs/tabletback.png")

		imgs=[self.tableton, self.tabletoff, self.tabletcam, self.tabletquiz, self.tabletback]

		desktop=QApplication.desktop()
		screen_geometry=desktop.screenGeometry()
		self.screen_width=screen_geometry.width()
		screen_height=screen_geometry.height()

		self.scalar=1

		if self.screen_width<1920:
			self.scalar=self.screen_width/1920
			for i in range(len(imgs)):
				imgs[i]=imgs[i].scaled(int(imgs[i].width()*self.scalar), int(imgs[i].height()*self.scalar))
				i+=1

		self.label=QLabel(self)
		self.label.setPixmap(self.tabletoff)
		self.label.setGeometry(0, 0, self.tabletoff.width(), self.tabletoff.height())
		self.setGeometry(int(self.screen_width/2)-int(self.tabletoff.width()/2), int(screen_height/2)-int(self.tabletoff.height()/2), self.tabletoff.width(), self.tabletoff.height())

		self.tablet_on=False
		self.cam_on=False
		self.light_on=False
		self.quiz_on=False
		self.safe_on=False
		self.flipped=False

		self.light=Light(50+self.pos().x(), self.pos().y()+55)

	def contextMenuEvent(self, event):
		menu = QMenu(self)
		close_action = menu.addAction("Exit")
		action = menu.exec_(self.mapToGlobal(event.pos()))

		if action == close_action:
			sys.exit()
		
	def mousePressEvent(self, event):
		if event.button()==Qt.LeftButton:
			if 44<=event.x()<=74 and 382<=event.y()<=412:
				if self.tablet_on:
					self.label.setPixmap(self.tabletoff)
					self.tablet_on=False
					self.cam_on=False
					self.light_on=False
					self.quiz_on=False
					self.safe_on=False
				else:
					self.label.setPixmap(self.tableton)
					self.tablet_on=True
			elif 51<=event.x()<=130 and 48<=event.y()<=128 and self.tablet_on:
				self.label.setPixmap(self.tabletcam)
				self.cam_on=True
			elif 165<=event.x()<=245 and 48<=event.y()<=128 and self.tablet_on:
				if self.light_on:
					self.light_on=False
					self.light.hide()
				else:
					self.light_on=True
					self.light.show()
			elif 279<=event.x()<=357 and 48<=event.y()<=128 and self.tablet_on:
				self.label.setPixmap(self.tabletquiz)
				self.quiz_on=True
			elif 745<=event.x()<=785 and 0<=event.y()<=40 and self.flipped==False:
				self.label.setPixmap(self.tabletback)
				self.flipped=True
				self.tablet_on=False
				self.quiz_on=False
				self.cam_on=False
				self.safe_on=False
				if self.light_on:
					self.light.tablet_flip()
			elif 0<=event.x()<=41 and 0<=event.y()<=40 and self.flipped:
				self.label.setPixmap(self.tabletoff)
				self.flipped=False
				if self.light_on:
					self.light.tablet_flip()
			elif 496<=event.x()<=578 and 233<=event.y()<=264 and self.quiz_on:
				self.label.setPixmap(self.tableton)
				self.quiz_on=False
			else:
				self.offset=event.pos()

	def mouseMoveEvent(self, event):
		if event.buttons()==Qt.LeftButton:
			old_pos=self.pos()
			self.move(event.globalPos() - self.offset)
			new_pos=self.pos()
			self.light.move(self.light.pos()+new_pos-old_pos)

class Light(QWidget):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.initUI(pos_x, pos_y)

	def initUI(self, pos_x, pos_y):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.light=QPixmap("imgs/light.png")
		self.label=QLabel(self)
		self.label.setPixmap(self.light)
		self.label.setGeometry(0, 0, self.light.width(), self.light.height())
		self.setGeometry(pos_x-int(self.light.width()/2), pos_y-int(self.light.height()/2), self.light.width(), self.light.height())

		self.tablet_flipped=False
	
	def tablet_flip(self):
		if self.tablet_flipped:
			self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
			self.move(self.pos().x()-685, self.pos().y())
			self.show()
			self.tablet_flipped=False
		else:
			self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
			self.show()
			self.move(self.pos().x()+685, self.pos().y())
			self.tablet_flipped=True

if __name__ == '__main__':
	app=QApplication(sys.argv)
	window=Tablet()
	window.show()	
	sys.exit(app.exec_())