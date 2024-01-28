import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMenu, QPushButton
from PyQt5.QtGui import QPixmap, QRegion, QFont
from PyQt5.QtCore import Qt, QTimer
from loader import Settings

class Tablet(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.setWindowTitle("GiftPacker")
		sett=Settings()

		self.tabletoff=QPixmap("imgs/tabletoff.png")
		self.tableton=QPixmap("imgs/tableton.png")
		self.tabletcam=QPixmap("imgs/tabletcam.png")
		self.tabletquiz=QPixmap("imgs/tabletquiz.png")
		self.tabletback=QPixmap("imgs/tabletback.png")
		self.sheet=QPixmap("imgs/sheet.png")
		self.quizmode=QPixmap("imgs/tabletquizmode.png")
		self.safe=QPixmap("imgs/safe.png")
		self.opensafe=QPixmap("imgs/safe_open.png")
		self.victory=QPixmap("imgs/finish.png")

		imgs=[self.tableton, self.tabletoff, self.tabletcam, self.tabletquiz, self.tabletback, self.sheet, self.quizmode, self.safe,
			self.opensafe, self.victory]

		desktop=QApplication.desktop()
		screen_geometry=desktop.screenGeometry()
		self.screen_width=screen_geometry.width()
		screen_height=screen_geometry.height()

		self.scalar=1

		if self.screen_width<1920:
			self.scalar=int(self.screen_width/1920)
			for i in range(len(imgs)):
				imgs[i]=imgs[i].scaled(imgs[i].width()*self.scalar, imgs[i].height()*self.scalar)
				i+=1

		self.label=QLabel(self)
		self.label.setPixmap(self.tabletoff)
		self.label.setGeometry(0, 0, self.tabletoff.width(), self.tabletoff.height())
		self.setGeometry((int(self.screen_width/2)-int(self.tabletoff.width()/2))*self.scalar, (int(screen_height/2)-int(self.tabletoff.height()/2))*self.scalar, self.tabletoff.width(), self.tabletoff.height())

		self.invisible_sheet=QLabel(self)
		self.invisible_sheet.setPixmap(self.sheet)
		self.invisible_sheet.setGeometry((-self.pos().x()+20)*self.scalar, (-self.pos().y()+20)*self.scalar, self.sheet.width(), self.sheet.height())

		i_s_txt=sett.mys1_msg
		self.invisible_sheet_txt=QLabel(i_s_txt, self)
		self.invisible_sheet_txt.setGeometry((-self.pos().x()+20)*self.scalar, (-self.pos().y()+20)*self.scalar, self.sheet.width(), int(self.sheet.height()/2))
		self.invisible_sheet_txt.setWordWrap(True)
		self.invisible_sheet_txt.lower()

		i_s_code=sett.mys1_code

		self.invisible_sheet_code=QLabel(i_s_code, self)
		self.invisible_sheet_code.setGeometry((-self.pos().x()+20)*self.scalar+int(self.sheet.width()/2), (-self.pos().y()+20)*self.scalar+int(self.sheet.height()*(2/3)),
											 int(self.sheet.width()/2), int(self.sheet.height()*(1/3)))
		self.invisible_sheet_code.setWordWrap(True)
		self.invisible_sheet_code.lower()

		self.invisible_sheet.lower()


		self.tablet_on=False
		self.cam_on=False
		self.light_on=False
		self.quiz_on=False
		self.safe_on=False
		self.flipped=False
		self.quiz_mode=False
		self.quiz_finished=False
		self.safe_open=False

		self.rolled_sheet=RolledSheet(self.pos().x(), self.pos().y(), self.width(), self.height(), self.scalar)

		self.light=Light((50+self.pos().x())*self.scalar, (self.pos().y()+55)*self.scalar, self.rolled_sheet, sett, self.scalar)

		self.questions=sett.questions
		self.answers=sett.answers

		self.question=QLabel("", self)
		self.question.setGeometry(360*self.scalar, 140*self.scalar, 400*self.scalar, 50*self.scalar)
		self.question.setWordWrap(True)
		self.question.setAlignment(Qt.AlignCenter)

		self.ans1=QLabel("", self)
		self.ans1.setGeometry(360*self.scalar, 220*self.scalar, 400*self.scalar, 50*self.scalar)
		self.ans1.setWordWrap(True)
		self.ans1.setAlignment(Qt.AlignLeft)

		self.ans2=QLabel("", self)
		self.ans2.setGeometry(360*self.scalar, 290*self.scalar, 400*self.scalar, 50*self.scalar)
		self.ans2.setWordWrap(True)
		self.ans2.setAlignment(Qt.AlignLeft)

		self.ans3=QLabel("", self)
		self.ans3.setGeometry(360*self.scalar, 360*self.scalar, 400*self.scalar, 50*self.scalar)
		self.ans3.setWordWrap(True)
		self.ans3.setAlignment(Qt.AlignLeft)

		self.question_index=0
		self.anses=[self.ans1, self.ans2, self.ans3]

		self.quiz_msg=sett.quiz_msg
		self.quiz_code=sett.quiz_code

		self.safe_password=sett.safe_code
		self.safe_input=QLabel("",self)
		self.safe_input.setAlignment(Qt.AlignCenter)
		self.safe_input.setGeometry(291*self.scalar, 104*self.scalar, 200*self.scalar, 33*self.scalar)
		
		self.safe_font = QFont()
		self.safe_font.setPointSize(30*self.scalar) 
		self.safe_input.setFont(self.safe_font)

		self.safe_msg=sett.rew_msg
		self.safe_code=sett.game_code

		self.victory_msg=QLabel(self.safe_msg, self)
		self.victory_msg.setWordWrap(True)
		self.victory_msg.setGeometry(50*self.scalar, 50*self.scalar, 685*self.scalar, 220*self.scalar)
		self.victory_msg.setAlignment(Qt.AlignCenter)
		self.victory_msg.setFont(self.safe_font)
		self.victory_msg.hide()

		self.victory_code=QLabel(self.safe_code, self)
		self.victory_code.setWordWrap(True)
		self.victory_code.setGeometry(50*self.scalar, 290*self.scalar, 685*self.scalar, 87*self.scalar)
		self.victory_code.setAlignment(Qt.AlignCenter)
		self.victory_code.setFont(self.safe_font)
		self.victory_code.hide()

		self.copy_button = QPushButton('Copy code', self)
		self.copy_button.move(650*self.scalar,345*self.scalar)
		self.copy_button.clicked.connect(self.copy)
		self.copy_button.hide()

	def contextMenuEvent(self, event):
		menu = QMenu(self)
		close_action = menu.addAction("Exit")
		action = menu.exec_(self.mapToGlobal(event.pos()))

		if action == close_action:
			sys.exit()
		
	def mousePressEvent(self, event):
		if event.button()==Qt.LeftButton:
			if 44*self.scalar<=event.x()<=74*self.scalar and 382*self.scalar<=event.y()<=412*self.scalar:
				if self.tablet_on:
					self.label.setPixmap(self.tabletoff)
					self.tablet_on=False
					self.cam_on=False
					self.light_on=False
					self.quiz_on=False
					self.safe_on=False
					self.quiz_mode=False
				else:
					self.label.setPixmap(self.tableton)
					self.tablet_on=True
			elif 51*self.scalar<=event.x()<=130*self.scalar and 48*self.scalar<=event.y()<=128*self.scalar and self.tablet_on: #kamera
				self.label.setPixmap(self.tabletcam)
				self.cam_on=True
				self.tablet_on=False
			elif 165*self.scalar<=event.x()<=245*self.scalar and 48*self.scalar<=event.y()<=128*self.scalar and self.tablet_on: #latarka
				if self.light_on:
					self.light_on=False
					self.light.hide()
				else:
					self.light_on=True
					self.light.show()
			elif 279*self.scalar<=event.x()<=357*self.scalar and 48*self.scalar<=event.y()<=128*self.scalar and self.tablet_on: #quiz
				self.label.setPixmap(self.tabletquiz)
				self.quiz_on=True
				self.tablet_on=False
			elif 745*self.scalar<=event.x()<=785*self.scalar and 0<=event.y()<=40*self.scalar and self.flipped==False: #flip
				self.label.setPixmap(self.tabletback)
				self.flipped=True
				self.tablet_on=False
				self.quiz_on=False
				self.cam_on=False
				self.safe_on=False
				self.quiz_mode=False
				self.setWindowFlags(Qt.FramelessWindowHint)
				self.show()
				if self.light_on:
					self.light.tablet_flip()
					if self.rolled_sheet.sheet_rolled==False:
						self.rolled_sheet.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
						self.rolled_sheet.show()
			elif 0<=event.x()<=41*self.scalar and 0<=event.y()<=40*self.scalar and self.flipped: #flip
				self.label.setPixmap(self.tabletoff)
				self.flipped=False
				self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
				self.show()
				if self.light_on:
					self.light.tablet_flip()
					if self.rolled_sheet.sheet_rolled==False:
						self.rolled_sheet.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
						self.rolled_sheet.show()
			elif 496*self.scalar<=event.x()<=578*self.scalar and 233*self.scalar<=event.y()<=264*self.scalar and self.quiz_on: #exit quiz
				self.label.setPixmap(self.tableton)
				self.quiz_on=False
				self.tablet_on=True
			elif 483*self.scalar<=event.x()<=590*self.scalar and 164*self.scalar<=event.y()<=194*self.scalar and self.quiz_on: #start quiz
				self.label.setPixmap(self.quizmode)
				self.quiz_mode=True
				self.question.setText(self.questions[0])
				self.ans1.setText(self.answers[0][0])
				self.ans2.setText(self.answers[0][1])
				self.ans3.setText(self.answers[0][2])
				self.question.show()
				self.ans1.show()
				self.ans2.show()
				self.ans3.show()
			elif 360*self.scalar<=event.x()<=760*self.scalar and 220*self.scalar<=event.y()<=270*self.scalar and self.quiz_mode:
				self.check_answer(1)
			elif 360*self.scalar<=event.x()<=760*self.scalar and 290*self.scalar<=event.y()<=340*self.scalar and self.quiz_mode:
				self.check_answer(2)
			elif 360*self.scalar<=event.x()<=760*self.scalar and 360*self.scalar<=event.y()<=410*self.scalar and self.quiz_mode:
				self.check_answer(3)
			elif 392*self.scalar<=event.x()<=470*self.scalar and 48*self.scalar<=event.y()<=128*self.scalar and self.tablet_on:
				self.tablet_on=False
				self.safe_on=True
				self.label.setPixmap(self.safe)
				self.safe_input.show()
			elif 292*self.scalar<=event.x()<=347*self.scalar and 166*self.scalar<=event.y()<=221*self.scalar and self.safe_on:
				self.safe_enter("1")
			elif 366*self.scalar<=event.x()<=420*self.scalar and 166*self.scalar<=event.y()<=221*self.scalar and self.safe_on:
				self.safe_enter("2")
			elif 438*self.scalar<=event.x()<=492*self.scalar and 166*self.scalar<=event.y()<=221*self.scalar and self.safe_on:
				self.safe_enter("3")
			elif 509*self.scalar<=event.x()<=563*self.scalar and 166*self.scalar<=event.y()<=221*self.scalar and self.safe_on:
				self.safe_enter("bc")
			elif 292*self.scalar<=event.x()<=347*self.scalar and 233*self.scalar<=event.y()<=287*self.scalar and self.safe_on:
				self.safe_enter("4")
			elif 366*self.scalar<=event.x()<=420*self.scalar and 233*self.scalar<=event.y()<=287*self.scalar and self.safe_on:
				self.safe_enter("5")
			elif 438*self.scalar<=event.x()<=492*self.scalar and 233*self.scalar<=event.y()<=287*self.scalar and self.safe_on:
				self.safe_enter("6")
			elif 509*self.scalar<=event.x()<=563*self.scalar and 233*self.scalar<=event.y()<=287*self.scalar and self.safe_on:
				self.safe_enter("en")
			elif 292*self.scalar<=event.x()<=347*self.scalar and 300*self.scalar<=event.y()<=354*self.scalar and self.safe_on:
				self.safe_enter("7")
			elif 366*self.scalar<=event.x()<=420*self.scalar and 300*self.scalar<=event.y()<=354*self.scalar and self.safe_on:
				self.safe_enter("8")
			elif 438*self.scalar<=event.x()<=492*self.scalar and 300*self.scalar<=event.y()<=354*self.scalar and self.safe_on:
				self.safe_enter("9")
			elif 509*self.scalar<=event.x()<=563*self.scalar and 300*self.scalar<=event.y()<=354*self.scalar and self.safe_on:
				self.safe_enter("0")
			elif 221*self.scalar<=event.x()<=403*self.scalar and 81*self.scalar<=event.y()<=192*self.scalar and self.safe_open:
				self.label.setPixmap(self.victory)
				self.victory_msg.show()
				self.victory_code.show()
				self.safe_on=True
				self.victory_msg.show()
				self.victory_code.show()
				self.copy_button.show()

			elif self.quiz_finished or self.safe_on:
				self.tablet_on=True
				self.quiz_on=False
				self.cam_on=False
				self.safe_on=False
				self.quiz_mode=False
				self.quiz_finished=False
				self.label.setPixmap(self.tableton)
				self.question.hide()
				self.question_index=0
				self.safe_input.hide()
				self.safe_open=False
				self.victory_msg.hide()
				self.victory_code.hide()
				self.copy_button.hide()
			
			self.offset=event.pos()

	def mouseMoveEvent(self, event):
		if event.buttons()==Qt.LeftButton:
			old_pos=self.pos()
			if self.rolled_sheet.sheet_rolled:
				self.rolled_sheet.move(self.pos().x()+self.width()-self.rolled_sheet.width(),
							self.pos().y()+self.height()-self.rolled_sheet.height()-25)
			self.move(event.globalPos() - self.offset)
			new_pos=self.pos()
			self.light.move(self.light.pos()+new_pos-old_pos)
			self.invisible_sheet.move(-self.pos().x()+20, -self.pos().y()+20)
			self.invisible_sheet_txt.move(-self.pos().x()+20, -self.pos().y()+20)
			self.invisible_sheet_code.move(-self.pos().x()+20+int(self.sheet.width()/2), -self.pos().y()+20+int(self.sheet.height()*(2/3)))
	def check_answer(self, ans):
		if self.answers[self.question_index][3]==ans:
			self.question_index+=1
			if len(self.questions)>self.question_index:
				self.question.setText(self.questions[self.question_index])
				self.ans1.setText(self.answers[self.question_index][0])
				self.ans2.setText(self.answers[self.question_index][1])
				self.ans3.setText(self.answers[self.question_index][2])
				self.ans1.show()
				self.ans2.show()
				self.ans3.show()
			else:
				self.question.setText(self.quiz_msg+"\n"+self.quiz_code)
				self.ans1.hide()
				self.ans2.hide()
				self.ans3.hide()
				self.quiz_mode=False
				self.quiz_finished=True
		else:
			self.anses[ans-1].hide()
	def safe_enter(self, inp):
		if inp in ["1","2","3","4","5","6","7","8","9","0"]:
			if len(self.safe_input.text())<6:
				self.safe_input.setText(self.safe_input.text()+inp)
		else:
			if inp=="bc":
				if len(self.safe_input.text())>0:
					self.safe_input.setText(self.safe_input.text()[0:-1])
			else:
				if self.safe_input.text()==self.safe_password:
					self.safe_input.hide()
					self.label.setPixmap(self.opensafe)
					self.safe_on=False
					self.safe_open=True
				else:
					self.safe_input.setText("")
	def copy(self):
		clipboard = QApplication.clipboard()
		clipboard.setText(self.victory_code.text())


class Light(QWidget):
	def __init__(self, pos_x, pos_y, rolled_sheet, sett, scalar):
		super().__init__()
		self.initUI(pos_x, pos_y, rolled_sheet, sett, scalar)

	def initUI(self, pos_x, pos_y, rolled_sheet, sett, scalar):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.scalar=scalar

		self.light=QPixmap("imgs/light.png")

		if self.scalar!=1:
			self.light=self.light.scaled(self.light.width()*self.scalar, self.light.height()*self.scalar)

		self.label=QLabel(self)
		self.label.setPixmap(self.light)
		self.label.setGeometry(0, 0, self.light.width(), self.light.height())
		self.setGeometry(pos_x-int(self.light.width()/2), pos_y-int(self.light.height()/2), self.light.width(), self.light.height())

		self.rolled_sheet=rolled_sheet

		i_s_txt=sett.mys2_msg
		self.sheet_txt=QLabel(i_s_txt, self)
		sheet_global_pos=self.mapFromGlobal(self.rolled_sheet.pos())
		self.sheet_txt.setGeometry(sheet_global_pos.x()+20, sheet_global_pos.y()+20,
							  self.rolled_sheet.sheet.width()-40, int(self.rolled_sheet.sheet.height()/2)-20)
		self.sheet_txt.setWordWrap(True)
		self.sheet_txt.lower()

		i_s_code=sett.mys2_code

		self.sheet_code=QLabel(i_s_code, self)
		self.sheet_code.setGeometry(sheet_global_pos.x()+20+int(self.rolled_sheet.sheet.width()/2),
							   sheet_global_pos.y()+20+int(self.rolled_sheet.sheet.height()*(2/3)),
											 int(self.rolled_sheet.sheet.width()/2)-40, int(self.rolled_sheet.sheet.height()*(1/3)))
		self.sheet_code.setWordWrap(True)
		self.sheet_code.lower()

		self.sheet_txt.hide()
		self.sheet_code.hide()

		region = QRegion(0, 0, self.light.width(), self.light.height(), QRegion.Ellipse)
		self.setMask(region)

		self.tablet_flipped=False

		self.rolled_timer=QTimer(self)
		self.rolled_timer.timeout.connect(self.is_rolled)
		self.rolled_timer.start(100)

		self.txt_pos=QTimer(self)
		self.txt_pos.timeout.connect(self.get_txt_pos)

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
	def is_rolled(self):
		if self.rolled_sheet.sheet_rolled==False:
			self.sheet_txt.show()
			self.sheet_code.show()
			self.rolled_timer.stop()
			self.txt_pos.start(20)
	def get_txt_pos(self):
		sheet_global_pos=self.mapFromGlobal(self.rolled_sheet.pos())
		self.sheet_txt.move(sheet_global_pos.x()+20, sheet_global_pos.y()+20)
		self.sheet_code.move(sheet_global_pos.x()+20+int(self.rolled_sheet.sheet.width()/2),
							   sheet_global_pos.y()+20+int(self.rolled_sheet.sheet.height()*(2/3)))

class RolledSheet(QWidget):
	def __init__(self, pos_x, pos_y, t_width, t_height, scalar):
		super().__init__()
		self.initUI(pos_x, pos_y, t_width, t_height, scalar)

	def initUI(self, pos_x, pos_y, t_width, t_height, scalar):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.scalar=scalar

		self.rolled=QPixmap("imgs/rolledsheet.png")
		self.sheet=QPixmap("imgs/sheet.png")

		if self.scalar!=1:
			self.rolled=self.rolled.scaled(self.rolled.width()*self.scalar, self.rolled.height()*self.scalar)
			self.sheet=self.sheet.scaled(self.sheet.width()*self.scalar, self.sheet.height()*self.scalar)


		self.label=QLabel(self)
		self.label.setPixmap(self.rolled)
		self.label.setGeometry(0, 0, self.rolled.width(), self.rolled.height())
		self.setGeometry(pos_x+t_width-self.rolled.width(), pos_y+t_height-self.rolled.height()-25, self.rolled.width(), self.rolled.height())

		self.sheet_rolled=True

	def mousePressEvent(self, event):
		if event.button()==Qt.LeftButton:
			self.offset=event.pos()

	def mouseMoveEvent(self, event):
		if event.buttons()==Qt.LeftButton:
			self.move(event.globalPos() - self.offset)
	
	def mouseDoubleClickEvent(self, event):
		if event.button() == Qt.LeftButton and self.sheet_rolled:
			self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
			self.label.setPixmap(self.sheet)
			self.label.setGeometry(0, 0, self.sheet.width(), self.sheet.height())
			self.setGeometry(self.pos().x(), self.pos().y(), self.sheet.width(), self.sheet.height())
			self.sheet_rolled=False
			self.show()


if __name__ == '__main__':
	app=QApplication(sys.argv)
	window=Tablet()
	window.show()	
	sys.exit(app.exec_())