import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QAction, QMenu
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class Tablet(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.tabletoff=QPixmap("imgs/tabletoff.png")
		self.tableton=QPixmap("imgs/tableton.png")
		self.tabletcam=QPixmap("imgs/tabletcam.png")
		self.tabletquiz=QPixmap("imgs/tabletquiz.png")

		imgs=[self.tableton, self.tabletoff, self.tabletcam, self.tabletquiz]

		desktop=QApplication.desktop()
		screen_geometry=desktop.screenGeometry()
		self.screen_width=screen_geometry.width()
		screen_height=screen_geometry.height()

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
			elif 279<=event.x()<=357 and 48<=event.y()<=128 and self.tablet_on:
				self.label.setPixmap(self.tabletquiz)
				self.quiz_on=True
			elif 496<=event.x()<=578 and 233<=event.y()<=264 and self.quiz_on:
				self.label.setPixmap(self.tableton)
				self.quiz_on=False
			else:
				self.offset=event.pos()

	def mouseMoveEvent(self, event):
		if event.buttons()==Qt.LeftButton:
			self.move(event.globalPos() - self.offset)

if __name__ == '__main__':
	app=QApplication(sys.argv)
	window=Tablet()
	window.show()	
	sys.exit(app.exec_())