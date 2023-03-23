
import sys
from PyQt5.QtWidgets import ( QPushButton,
                             QLineEdit, QMessageBox
                             )
from PyQt5.QtWidgets import  QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtWidgets import  QWidget, QDesktopWidget

from end import End
from PyQt5 import  QtGui, QtCore
import os

class Equipment(QWidget):
    def __init__(self, activevar, path, counter, first_aray, parent=None):
        super(Equipment, self).__init__(parent)
        #self.setFont(QtGui.QFont('Arial', 12))
        self.setFont(QtGui.QFont('B Nazanin', 12))
        self.checks()
        self.mainLayout = QHBoxLayout()
        self.firstVertical = QVBoxLayout()
        self.secondVertical = QVBoxLayout()
        self.thirdVetical = QVBoxLayout()
        self.fourthVertical = QVBoxLayout()
        self.fifthVertical = QVBoxLayout()

        myscreen = QDesktopWidget().screenGeometry()

        mywidth = myscreen.width() * 70 / 100
        myheight = myscreen.height() * 55 / 100
        self.setMinimumSize(int(mywidth), int(myheight))
        self.center()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))
        self.setWindowTitle('equipment')
        self.path = path
        self.counter = counter
        self.myar = first_aray
        self.activevar = activevar
       # print('we came there equipment')
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Efficiency of available tools')
        self.line = QLineEdit(self)
        self.line.move(300, 20)
        self.line.resize(25, 25)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line)
        self.nameLabel.move(340, 20)
        self.nameLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Accuracy of available tools ')
        self.line2 = QLineEdit(self)
        self.line2.move(300, 60)
        self.line2.resize(25, 25)
        self.line2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line2)
        self.nameLabel2.move(340, 60)
        self.nameLabel2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel2)

        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Being healthy of available tools ')
        self.line3 = QLineEdit(self)
        self.line3.move(300, 100)
        self.line3.resize(25, 25)
        self.line3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line3)
        self.nameLabel3.move(340, 100)
        self.nameLabel3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel3)

        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('User-friendly of available tools')
        self.line4 = QLineEdit(self)
        self.line4.move(300, 140)
        self.line4.resize(25, 25)
        self.line4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line4)
        self.nameLabel4.move(340, 140)
        self.nameLabel4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel4)

        self.nameLabel5 = QLabel(self)
        self.nameLabel5.setText('Life span of existing device')
        self.line5 = QLineEdit(self)
        self.line5.move(300, 180)
        self.line5.resize(25, 25)
        self.line5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line5)
        self.nameLabel5.move(340, 180)
        self.nameLabel5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel5)

        self.nameLabel6 = QLabel(self)
        self.nameLabel6.setText('Fit of existing instrument to anatomy')
        self.line6 = QLineEdit(self)
        self.line6.move(300, 220)
        self.line6.resize(25, 25)
        self.line6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line6)
        self.nameLabel6.move(340, 220)
        self.nameLabel6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel6)

        self.nameLabel526 = QLabel(self)
        self.nameLabel526.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel526.setText('Question 6:')
        self.nameLabel526.move(20, 221)
        self.nameLabel526.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fourthVertical.addWidget(self.nameLabel526)

        self.nameLabel550 = QLabel(self)
        self.nameLabel550.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel550.setText('yes -> 1')
        self.nameLabel550.move(100, 220)
        self.nameLabel550.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fourthVertical.addWidget(self.nameLabel550)

        self.nameLabel5117 = QLabel(self)
        self.nameLabel5117.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel5117.setText('no -> 2')
        self.nameLabel5117.move(100, 235)
        self.nameLabel5117.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fourthVertical.addWidget(self.nameLabel5117)



        self.nameLabel7 = QLabel(self)
        self.nameLabel7.setText('Degree of biocompatibility of existing tools')
        self.line7 = QLineEdit(self)
        self.line7.move(300, 260)
        self.line7.resize(25, 25)
        self.line7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line7)
        self.nameLabel7.move(340, 260)
        self.nameLabel7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel7)

        self.nameLabel8 = QLabel(self)
        self.nameLabel8.setText('Optimal size of available tools')
        self.line8 = QLineEdit(self)
        self.line8.move(300, 300)
        self.line8.resize(25, 25)
        self.line8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line8)
        self.nameLabel8.move(340, 300)
        self.nameLabel8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel8)

        self.nameLabel508 = QLabel(self)
        self.nameLabel508.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel508.setText('Question 1 to 3')
        self.nameLabel508.move(10, 111)
        self.nameLabel508.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel508)

        self.nameLabel5118 = QLabel(self)
        self.nameLabel5118.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel5118.setText('And Question 7 to 8 :')
        self.nameLabel5118.move(10, 127)
        self.nameLabel5118.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel5118)

        self.nameLabel525 = QLabel(self)
        self.nameLabel525.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel525.setText('None -> 0')
        self.nameLabel525.move(100, 90)
        self.nameLabel525.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel525)

        self.nameLabel5226 = QLabel(self)
        self.nameLabel5226.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel5226.setText('low -> 3')
        self.nameLabel5226.move(100, 105)
        self.nameLabel5226.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel5226)

        self.nameLabel5117 = QLabel(self)
        self.nameLabel5117.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel5117.setText('medium -> 2')
        self.nameLabel5117.move(100, 120)
        self.nameLabel5117.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel5117)

        self.nameLabel528 = QLabel(self)
        self.nameLabel528.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel528.setText('high -> 1')
        self.nameLabel528.move(100, 135)
        self.nameLabel528.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel528)


        self.nameLabel9 = QLabel(self)
        self.nameLabel9.setText('تاثیر استفاده از ابزار جدید بر کارایی کاربر :')
        self.line9 = QLineEdit(self)
        self.line9.move(300, 350)
        self.line9.resize(25, 25)
        self.line9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line9)
        self.nameLabel9.move(340, 350)
        self.nameLabel9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel9)

        self.nameLabel588 = QLabel(self)
        self.nameLabel588.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel588.setText('Question 9 :')
        self.nameLabel588.move(20, 351)
        self.nameLabel588.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel588)

        self.nameLabel55 = QLabel(self)
        self.nameLabel55.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel55.setText('None -> 0')
        self.nameLabel55.move(100, 330)
        self.nameLabel55.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel55)

        self.nameLabel56 = QLabel(self)
        self.nameLabel56.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel56.setText('low -> 1')
        self.nameLabel56.move(100, 345)
        self.nameLabel56.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel56)

        self.nameLabel57 = QLabel(self)
        self.nameLabel57.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel57.setText('medium -> 2')
        self.nameLabel57.move(100, 360)
        self.nameLabel57.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel57)

        self.nameLabel58 = QLabel(self)
        self.nameLabel58.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel58.setText('high -> 3')
        self.nameLabel58.move(100, 375)
        self.nameLabel58.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel58)

        self.nameLabel5842 = QLabel(self)
        self.nameLabel5842.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel5842)

        self.pb = QPushButton('ok', self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(self.button_click1)
        self.pb.resize(100, 40)
        self.pb.move(280, 400)
        self.pb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.pb)

        # self.FourthVertical.addStretch(45)
        self.thirdVetical.addStretch(5)
        self.fourthVertical.addStretch(5)
        self.fifthVertical.addStretch(5)

        self.mainLayout.addLayout(self.fifthVertical)
        self.mainLayout.addLayout(self.fourthVertical)
        self.mainLayout.addLayout(self.thirdVetical)
        self.mainLayout.addLayout(self.secondVertical)
        self.mainLayout.addLayout(self.firstVertical)

        self.setLayout(self.mainLayout)

    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

        #print(self.size(),'size')

    # noinspection PyTypeChecker
    def button_click1(self):
      #print('i m here in ok')
      if self.line.text() == '' or self.line2.text() == '' or self.line3.text() == '' or self.line4.text() == ''or self.line5.text() == '' or \
        self.line6.text() == '' or self.line7.text() == '' or self.line8.text() == '' or self.line9.text() == '':
            msg1 = QMessageBox(self)
            self.messageBox = msg1
            msg1.setText('please full the blank!')
            msg1.setWindowTitle('Alert')
            msg1.resize(600, 400)
            # print('came oweeeer')
            msg1.show()
      elif (
              self.line.text() != '1' and self.line.text() != '2' and self.line.text() != '3' and self.line.text() != '0'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (
              self.line2.text() != '1' and self.line2.text() != '2' and self.line2.text() != '3' and self.line2.text() != '0'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (
              self.line3.text() != '1' and self.line3.text() != '2' and self.line3.text() != '3' and self.line3.text() != '0'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (
              self.line4.text() != '1' and self.line4.text() != '2' and self.line4.text() != '3' and self.line4.text() != '0'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (
              self.line5.text() != '1' and self.line5.text() != '2' and self.line5.text() != '3' and self.line5.text() != '0'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (
              self.line6.text() != '2' and self.line6.text() != '1'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (
              self.line7.text() != '2' and self.line7.text() != '1' and self.line7.text() != '0' and self.line7.text() != '3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (
              self.line8.text() != '2' and self.line8.text() != '1' and self.line8.text() != '0' and self.line8.text() != '3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (
              self.line9.text() != '2' and self.line9.text() != '1' and self.line9.text() != '0' and self.line9.text() != '3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      else:
        numb = self.line.text()
        numb2 = self.line2.text()
        numb3 = self.line3.text()
        numb4 = self.line4.text()
        numb5 = self.line5.text()
        numb6 = self.line6.text()
        numb7 = self.line7.text()
        numb8 = self.line8.text()
        numb9 = self.line9.text()
        # print(numb,numb4,numb2,numb3)
        # print(type(int(numb3)),'my type')
        avg = (int(numb)*2 + int(numb2)*4 + int(numb3)*2 + int(numb4)*2 +int(numb5)*2 + int(numb6)*1 + int(numb7)*4 + int(numb8)*2
               + int(numb9)*4 ) / 23
        avg = format(avg, '.2f')
        avg = 'total score is '+ str(avg)
        file = open(self.path, "a")
        file.write("equipment " + avg + "\n")
        file.close()
       # print(avg,'is sum. ')
        msg = QMessageBox(self)
        self.messageBox = msg
        msg.setText(avg)
        msg.setWindowTitle('Score')
        msg.resize(600,400)

        msg.show()
        self.hide()
        self.counter -= 1
        if self.counter == 0 :
            self.end_page = End(self.activevar, self.myar, self.path)
            self.end_page.show()

