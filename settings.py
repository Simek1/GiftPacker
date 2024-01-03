import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTabWidget, QTextEdit, QLineEdit, QRadioButton
from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject

class MyForm(QWidget):
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
        self.lineEdit_3 = QLineEdit(self.mys1)
        self.lineEdit_3.setGeometry(QRect(10, 220, 31, 20))
        self.textEdit_2 = QTextEdit(self.mys1)
        self.textEdit_2.setGeometry(QRect(10, 20, 191, 161))
        self.tabs.addTab(self.mys1, "Invisible sheet")

        self.mys2 = QWidget()
        self.label_6 = QLabel(self.mys2)
        self.label_6.setGeometry(QRect(200, 160, 231, 21))
        self.label_7 = QLabel(self.mys2)
        self.label_7.setGeometry(QRect(50, 220, 141, 21))
        self.lineEdit_4 = QLineEdit(self.mys2)
        self.lineEdit_4.setGeometry(QRect(10, 220, 31, 20))
        self.textEdit_3 = QTextEdit(self.mys2)
        self.textEdit_3.setGeometry(QRect(10, 20, 191, 161))
        self.tabs.addTab(self.mys2, "Hidden sheet")

        self.quiz = QWidget()
        self.lineEdit_5 = QLineEdit(self.quiz)
        self.lineEdit_5.setGeometry(QRect(10, 20, 61, 20))
        self.label_8 = QLabel(self.quiz)
        self.label_8.setGeometry(QRect(80, 20, 101, 16))
        self.conf_q = QPushButton("Confirm", self.quiz)
        self.conf_q.setGeometry(QRect(200, 20, 61, 23))
        self.conf_q.clicked.connect(self.confirm_questions)
        self.lineEdit_6 = QLineEdit(self.quiz)
        self.lineEdit_6.setGeometry(QRect(10, 270, 31, 20))
        self.label_14 = QLabel(self.quiz)
        self.label_14.setGeometry(QRect(200, 210, 231, 21))
        self.label_15 = QLabel(self.quiz)
        self.label_15.setGeometry(QRect(50, 270, 141, 21))
        self.textEdit_8 = QTextEdit(self.quiz)
        self.textEdit_8.setGeometry(QRect(10, 70, 191, 161))
        self.tabs.addTab(self.quiz, "Quiz")

        self.safe = QWidget()
        self.lineEdit_2 = QLineEdit(self.safe)
        self.lineEdit_2.setGeometry(QRect(10, 60, 113, 20))
        self.label_3 = QLabel(self.safe)
        self.label_3.setGeometry(QRect(130, 60, 61, 16))
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

        self.label_3.setText("Safe code")

    def confirm_questions(self):
        pass
    def create_question_tab(self, number):
        self.tab_3 = QWidget()
        self.textEdit_4 = QTextEdit(self.tab_3)
        self.textEdit_4.setGeometry(QRect(0, 10, 351, 71))
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setGeometry(QRect(390, 65, 61, 21))
        self.textEdit_5 = QTextEdit(self.tab_3)
        self.textEdit_5.setGeometry(QRect(0, 120, 351, 31))
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setGeometry(QRect(390, 130, 81, 31))
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setGeometry(QRect(390, 200, 81, 31))
        self.textEdit_6 = QTextEdit(self.tab_3)
        self.textEdit_6.setGeometry(QRect(0, 190, 351, 31))
        self.label_12 = QLabel(self.tab_3)
        self.label_12.setGeometry(QRect(390, 270, 81, 31))
        self.textEdit_7 = QTextEdit(self.tab_3)
        self.textEdit_7.setGeometry(QRect(0, 260, 351, 31))
        self.radioButton = QRadioButton(self.tab_3)
        self.radioButton.setGeometry(QRect(360, 130, 16, 17))
        self.radioButton_2 = QRadioButton(self.tab_3)
        self.radioButton_2.setGeometry(QRect(360, 200, 16, 17))
        self.radioButton_3 = QRadioButton(self.tab_3)
        self.radioButton_3.setGeometry(QRect(360, 270, 16, 17))
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setGeometry(QRect(0, 300, 321, 16))
        self.tabs.addTab(self.tab_3, "Question")

        self.label_9.setText("Question")
        self.label_10.setText("First answer")
        self.label_11.setText("Second answer")
        self.label_12.setText("Third answer")
        self.label_13.setText("Check the right answer")
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())
