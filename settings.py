import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTabWidget, QTextEdit, QLineEdit, QRadioButton
from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QIntValidator



class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(510, 366)

        self.tabs = QTabWidget(self)
        self.tabs.setGeometry(QRect(0, 0, 511, 341))

        self.rew_tab = QWidget()
        self.game_code = QLineEdit(self.rew_tab)
        self.game_code.setGeometry(QRect(10, 220, 191, 20))
        self.label = QLabel(self.rew_tab)
        self.label.setGeometry(QRect(200, 220, 111, 21))
        self.rew_msg = QTextEdit(self.rew_tab)
        self.rew_msg.setGeometry(QRect(10, 20, 191, 161))
        self.label_2 = QLabel(self.rew_tab)
        self.label_2.setGeometry(QRect(210, 160, 111, 21))
        self.tabs.addTab(self.rew_tab, "Reward")

        self.mys1 = QWidget()
        self.label_4 = QLabel(self.mys1)
        self.label_4.setGeometry(QRect(200, 160, 231, 21))
        self.label_5 = QLabel(self.mys1)
        self.label_5.setGeometry(QRect(50, 220, 141, 21))
        self.mys1_code = QLineEdit(self.mys1)
        self.mys1_code.setGeometry(QRect(10, 220, 31, 20))
        self.mys1_code.setValidator(QIntValidator())
        self.mys1_code.setMaxLength(2)
        self.mys1_msg = QTextEdit(self.mys1)
        self.mys1_msg.setGeometry(QRect(10, 20, 191, 161))
        self.tabs.addTab(self.mys1, "Invisible sheet")

        self.mys2 = QWidget()
        self.label_6 = QLabel(self.mys2)
        self.label_6.setGeometry(QRect(200, 160, 231, 21))
        self.label_7 = QLabel(self.mys2)
        self.label_7.setGeometry(QRect(50, 220, 141, 21))
        self.mys2_code = QLineEdit(self.mys2)
        self.mys2_code.setGeometry(QRect(10, 220, 31, 20))
        self.mys2_code.setValidator(QIntValidator())
        self.mys2_code.setMaxLength(2)
        self.mys2_msg = QTextEdit(self.mys2)
        self.mys2_msg.setGeometry(QRect(10, 20, 191, 161))
        self.tabs.addTab(self.mys2, "Hidden sheet")

        self.quiz = QWidget()
        self.questions_num = QLineEdit(self.quiz)
        self.questions_num.setGeometry(QRect(10, 20, 61, 20))
        self.questions_num.setValidator(QIntValidator())
        self.label_8 = QLabel(self.quiz)
        self.label_8.setGeometry(QRect(80, 20, 101, 16))
        self.conf_q = QPushButton("Confirm", self.quiz)
        self.conf_q.setGeometry(QRect(200, 20, 61, 23))
        self.conf_q.clicked.connect(self.confirm_questions)
        self.quiz_code = QLineEdit(self.quiz)
        self.quiz_code.setGeometry(QRect(10, 270, 31, 20))
        self.quiz_code.setValidator(QIntValidator())
        self.quiz_code.setMaxLength(2)
        self.label_14 = QLabel(self.quiz)
        self.label_14.setGeometry(QRect(200, 210, 231, 21))
        self.label_15 = QLabel(self.quiz)
        self.label_15.setGeometry(QRect(50, 270, 141, 21))
        self.quiz_msg = QTextEdit(self.quiz)
        self.quiz_msg.setGeometry(QRect(10, 70, 191, 161))
        self.tabs.addTab(self.quiz, "Quiz")
        self.question_tabs=[]

        self.safe = QWidget()
        self.safe_code = QLineEdit(self.safe)
        self.safe_code.setGeometry(QRect(10, 60, 113, 20))
        self.safe_code.setValidator(QIntValidator())
        self.safe_code.setMaxLength(6)
        self.label_3 = QLabel(self.safe)
        self.label_3.setGeometry(QRect(130, 60, 100, 16))
        self.tabs.addTab(self.safe, "Safe code")

        self.end_button = QPushButton("End configuration", self)
        self.end_button.setGeometry(QRect(404, 340, 101, 23))

        self.setWindowTitle("GiftPacker")

        self.label.setText("* Game code")
        self.label_2.setText("Message")

        self.label_4.setText("* Message suggesting the order of safe codes")
        self.label_5.setText("Part of safe code (2 digits)")

        self.label_6.setText("* Message suggesting the order of safe codes")
        self.label_7.setText("Part of safe code (2 digits)")

        self.label_8.setText("Number of questions")
        self.label_14.setText("* Message suggesting the order of safe codes")
        self.label_15.setText("Part of safe code (2 digits)")

        self.label_3.setText("Safe code (6 digits)")

    def confirm_questions(self):
        i=len(self.question_tabs)
        while i < int(self.questions_num.text()):
            self.create_question_tab(i)
            i+=1
        if i > int(self.questions_num.text()):
            for j in range(int(self.questions_num.text()), i):
                self.tabs.removeTab(self.tabs.count()-1)
                j+=1
            del(self.question_tabs[int(self.questions_num.text()):])
            print(self.question_tabs)

    def create_question_tab(self, num):
        self.question_tabs.append(QuestionTab())
        self.tabs.addTab(self.question_tabs[num], f"Question {num+1}")      

class QuestionTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
    def init(self):
        self.q_question = QTextEdit(self)
        self.q_question.setGeometry(QRect(0, 10, 351, 71))
        self.label1 = QLabel(self)
        self.label1.setGeometry(QRect(390, 65, 61, 21))
        self.q_ans1 = QTextEdit(self)
        self.q_ans1.setGeometry(QRect(0, 120, 351, 31))
        self.label2 = QLabel(self)
        self.label2.setGeometry(QRect(390, 130, 81, 31))
        self.label3 = QLabel(self)
        self.label3.setGeometry(QRect(390, 200, 81, 31))
        self.q_ans2 = QTextEdit(self)
        self.q_ans2.setGeometry(QRect(0, 190, 351, 31))
        self.label4 = QLabel(self)
        self.label4.setGeometry(QRect(390, 270, 81, 31))
        self.q_ans3 = QTextEdit(self)
        self.q_ans3.setGeometry(QRect(0, 260, 351, 31))
        self.radioButton = QRadioButton(self)
        self.radioButton.setGeometry(QRect(360, 130, 16, 17))
        self.radioButton2 = QRadioButton(self)
        self.radioButton2.setGeometry(QRect(360, 200, 16, 17))
        self.radioButton3 = QRadioButton(self)
        self.radioButton3.setGeometry(QRect(360, 270, 16, 17))
        self.label5 = QLabel(self)
        self.label5.setGeometry(QRect(0, 300, 321, 16))

        self.label1.setText("Question")
        self.label2.setText("First answer")
        self.label3.setText("Second answer")
        self.label4.setText("Third answer")
        self.label5.setText("Check the right answer")
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SettingsWindow()
    window.show()
    sys.exit(app.exec_())
