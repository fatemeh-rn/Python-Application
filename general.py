
import sys
from PyQt5.QtWidgets import (QApplication,
                              QPushButton,
                             QLineEdit, QMessageBox,)
from PyQt5.QtWidgets import  QLabel,QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtWidgets import  QWidget, QDesktopWidget
from PyQt5 import  QtGui, QtCore
import os
from market import Market
from it import It

class General(QWidget):
    def __init__(self,activevar, op1, op2, op3,op4, path, counter, first_ary, ItOpen, parent=None):
        super(General, self).__init__(parent)
        print('ingernerallll')
        self.checks()
       # self.setFont(QtGui.QFont('Arial', 12))
        self.setFont(QtGui.QFont('B Nazanin', 12))
        self.mainLayout = QHBoxLayout()
        self.firstVertical = QVBoxLayout()
        self.secondVertical = QVBoxLayout()
        self.ThirdVetical = QVBoxLayout()
        self.FourthVertical = QVBoxLayout()
        self.fifthVertical = QVBoxLayout()
        self.sixthVertical = QVBoxLayout()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))
        #mai = Window()
        self.ItOpen = ItOpen
        self.path = path
        self.myar = first_ary
        self.path = path
        self.activevar = activevar
        self.setWindowTitle('general')
        # self.setMaximumWidth(2000)
        myscreen = QDesktopWidget().screenGeometry()

        mywidth = myscreen.width() * 80 / 100
        myheight = myscreen.height() * 55 / 100
        self.setMinimumSize(int(mywidth), int(myheight))
        self.center()
        self.counter = counter
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Number of times that need has been observed')
        self.nameLabel.move(340, 20)
        self.nameLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel)

        print('this is after namelabel1')

        self.line = QLineEdit(self)
        self.line.move(300, 20)
        self.line.resize(25, 25)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line)

        print('this is after LINE')

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Interest rate of team')
        self.nameLabel2.move(340, 70)
        self.nameLabel2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel2)
        print('this is after LINE2')
        self.line2 = QLineEdit(self)
        self.line2.move(300, 70)
        self.line2.resize(25, 25)
        self.line2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line2)

        print('this is after LINE21')
        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Amount of skill and knowledge of team')
        self.nameLabel3.move(340, 120)
        self.nameLabel3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel3)
        print('this is after LINE3')
        self.line3 = QLineEdit(self)
        self.line3.move(300, 120)
        self.line3.resize(25, 25)
        self.line3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line3)
        print('this is after LINE32')
        self.nameLabel538 = QLabel(self)
        self.nameLabel538.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel538.setText('Question 1 to 3:')
        #self.nameLabel538.ssetAlignment(Qt.AlignLeft)
        #self.nameLabel538.move(20, 65)
        self.nameLabel538.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ThirdVetical.addWidget(self.nameLabel538)
        self.nameLabel35 = QLabel(self)
        self.nameLabel35.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel35.setText('low -> 1')
        #self.nameLabel35.move(100, 50)
        self.nameLabel35.resize(50, 30)
        self.nameLabel35.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ThirdVetical.addWidget(self.nameLabel35)
        print('this is after LINE35')
        self.nameLabel36 = QLabel(self)
        self.nameLabel36.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel36.setText('medium -> 2')
        #self.nameLabel36.move(100, 65)
        self.nameLabel36.resize(80, 30)
        self.nameLabel36.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ThirdVetical.addWidget(self.nameLabel36)
        print('this is after LINE36')
        self.nameLabel37 = QLabel(self)
        self.nameLabel37.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel37.setText('high -> 3')
        #self.nameLabel37.move(100, 80)
        self.nameLabel37.resize(70, 30)
        self.nameLabel37.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ThirdVetical.addWidget(self.nameLabel37)
        print('this is after LINE37')

        print('this is after LINE38')
        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('Number of disease area covered by need')
        self.nameLabel4.move(340, 170)
        self.nameLabel4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel4)
        print('this is after LINE4')
        self.line4 = QLineEdit(self)
        self.line4.move(300, 170)
        self.line4.resize(25, 25)
        self.line4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line4)
        print('this is after LINE41')
        self.nameLabel528 = QLabel(self)
        self.nameLabel528.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel528.setText('Question 4:')
        #self.nameLabel528.move(20, 175)
        self.nameLabel528.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.FourthVertical.addWidget(self.nameLabel528)

        self.nameLabel45 = QLabel(self)
        self.nameLabel45.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel45.setText('1 -> 1')
        #self.nameLabel45.move(100, 160)
        self.nameLabel45.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.FourthVertical.addWidget(self.nameLabel45)
        print('this is after LINE45')
        self.nameLabel46 = QLabel(self)
        self.nameLabel46.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel46.setText('1-3 -> 2')
        #self.nameLabel46.move(100, 175)
        self.nameLabel46.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.FourthVertical.addWidget(self.nameLabel46)
        print('this is after LINE46')

        self.nameLabel48 = QLabel(self)
        self.nameLabel48.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel48.setText('more than 3 -> 3')
        #self.nameLabel4116.move(100, 190)
        self.nameLabel48.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.FourthVertical.addWidget(self.nameLabel48)



        self.nameLabel5 = QLabel(self)
        self.nameLabel5.setText('Available therapies')
        self.nameLabel5.move(340, 230)
        self.nameLabel5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel5)

        self.line5 = QLineEdit(self)
        self.line5.move(300, 230)
        self.line5.resize(25, 25)
        self.line5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line5)

        self.nameLabel518 = QLabel(self)
        self.nameLabel518.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel518.setText('Question 5:')
        #self.nameLabel518.move(20, 241)
        #self.nameLabel518.ssetAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.nameLabel518.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel518)

        self.nameLabel55 = QLabel(self)
        self.nameLabel55.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel55.setText('None -> 4')
        #self.nameLabel55.move(100, 220)
        self.nameLabel55.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel55)

        self.nameLabel56 = QLabel(self)
        self.nameLabel56.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel56.setText('low -> 3')
        #self.nameLabel56.move(100, 235)
        self.nameLabel56.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel56)

        self.nameLabel57 = QLabel(self)
        self.nameLabel57.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel57.setText('medium -> 2')
        #self.nameLabel57.move(100, 250)
        self.nameLabel57.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel57)

        self.nameLabel58 = QLabel(self)
        self.nameLabel58.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel58.setText('high -> 1')
        #self.nameLabel58.move(100, 265)
        self.nameLabel58.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel58)

        self.nameLabel6 = QLabel(self)
        self.nameLabel6.setText('Impact of possible new ways on reducing potential costs in need area')
        self.nameLabel6.move(340, 280)
        self.nameLabel6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel6)

        self.line6 = QLineEdit(self)
        self.line6.move(300, 280)
        self.line6.resize(25, 25)
        self.line6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line6)


        self.nameLabel7 = QLabel(self)
        self.nameLabel7.setText('Degree of complexity of technology required to responding need')
        self.nameLabel7.move(340, 320)
        self.nameLabel7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel7)

        self.line7 = QLineEdit(self)
        self.line7.move(300, 320)
        self.line7.resize(25, 25)
        self.line7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line7)


        self.nameLabel8 = QLabel(self)
        self.nameLabel8.setText('Effect of need satisfaction on saving time on target population ')
        self.nameLabel8.move(340, 370)
        self.nameLabel8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel8)

        self.line8 = QLineEdit(self)
        self.line8.move(300, 370)
        self.line8.resize(25, 25)
        self.line8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line8)


        self.nameLabel9 = QLabel(self)
        self.nameLabel9.setText('Psychological impact of need satisfaction on target population')
        self.nameLabel9.move(340, 420)
        self.nameLabel9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel9)

        self.line9 = QLineEdit(self)
        self.line9.move(300, 420)
        self.line9.resize(25, 25)
        self.line9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line9)


        self.nameLabel10 = QLabel(self)
        self.nameLabel10.setText('Vitality of need from assessor perspective')
        self.nameLabel10.move(340, 470)
        self.nameLabel10.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel10)

        self.line10 = QLineEdit(self)
        self.line10.move(300, 470)
        self.line10.resize(25, 25)
        self.line10.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line10)


        self.nameLabel11 = QLabel(self)
        self.nameLabel11.setText('Probability of need satisfaction')
        self.nameLabel11.move(340, 520)
        self.nameLabel11.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel11)

        self.line11 = QLineEdit(self)
        self.line11.move(300, 520)
        self.line11.resize(25, 25)
        self.line11.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line11)


        self.nameLabel12 = QLabel(self)
        self.nameLabel12.setText('Effect of need satisfaction on increasing of life quality of target population ')
        self.nameLabel12.move(340, 570)
        self.nameLabel12.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel12)

        self.line12 = QLineEdit(self)
        self.line12.move(300, 570)
        self.line12.resize(25, 25)
        self.line12.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line12)


        self.nameLabel13 = QLabel(self)
        self.nameLabel13.setText('In case of any conflict, degree of confliction between stakeholders')
        self.nameLabel13.move(340, 620)
        self.nameLabel13.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel13)

        self.line13 = QLineEdit(self)
        self.line13.move(300, 620)
        self.line13.resize(25, 25)
        self.line13.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line13)


        self.nameLabel1113 = QLabel(self)
       # self.nameLabel13.setText('سوال 13 متیبم سیمبسمی مندسیمنب منسیمنب منمسیب تمنتمسیب منمسیب منتمیب متمب ی:')
        self.nameLabel1113.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel1113)

        self.nameLabel100 = QLabel(self)
        self.nameLabel100.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel100.setText('Question 6 to 13:')
      #  self.nameLabel100.ssetAlignment(Qt.AlignLeft | Qt.AlignTop)
        #self.nameLabel100.move(5, 461)
        self.nameLabel100.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sixthVertical.addWidget(self.nameLabel100)

        self.nameLabel68 = QLabel(self)
        self.nameLabel68.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel68.setText('None -> 0')
        #self.nameLabel68.move(100, 425)
        self.nameLabel68.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sixthVertical.addWidget(self.nameLabel68)

        self.nameLabel78 = QLabel(self)
        self.nameLabel78.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel78.setText('low -> 1')
        #self.nameLabel78.move(100, 440)
        self.nameLabel78.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sixthVertical.addWidget(self.nameLabel78)

        self.nameLabel78888 = QLabel(self)
        self.nameLabel78888.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel78888.setText('medium -> 2')
        #self.nameLabel78.move(100, 440)
        self.nameLabel78888.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sixthVertical.addWidget(self.nameLabel78888)

        self.nameLabel78889 = QLabel(self)
        self.nameLabel78889.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel78889.setText('high -> 3')
        #self.nameLabel78.move(100, 440)
        self.nameLabel78889.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sixthVertical.addWidget(self.nameLabel78889)

        self.nameLabel88 = QLabel(self)
        #self.nameLabel88.setText('medium -> 2')
        self.nameLabel88.move(100, 455)
        self.nameLabel88.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sixthVertical.addWidget(self.nameLabel88)


        self.pb = QPushButton('ok', self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(lambda :self.button_click3(op1, op2, op3, op4))
        self.pb.resize(100, 40)
        self.pb.move(280, 650)
        self.pb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.pb)

        #self.FourthVertical.addStretch(45)
        self.ThirdVetical.addStretch(2)
        self.FourthVertical.addStretch(2)
        self.fifthVertical.addStretch(2)
        self.sixthVertical.addStretch(2)
        #self.FourthVertical.setAlignment(Qt.)
        print('this is after LINEMAIN1')
        self.mainLayout.addLayout(self.sixthVertical)
        self.mainLayout.addLayout(self.fifthVertical)
        self.mainLayout.addLayout(self.FourthVertical)

        self.mainLayout.addLayout(self.ThirdVetical)

        self.mainLayout.addLayout(self.secondVertical)

        self.mainLayout.addLayout(self.firstVertical)

        self.setLayout(self.mainLayout)

    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)

    def center(self):
       # print('come to senter')
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        #print(self.size(),'size')

    # noinspection PyTypeChecker
    def button_click3(self,op1, op2, op3, op4):
     # print('i m here in ok')
      if self.line.text() == '' or self.line2.text() == '' or self.line3.text() == '' or self.line4.text() == '' or self.line5.text() == '' or self.line6.text() == '' \
              or self.line7.text() == '' or self.line8.text() == '' or self.line9.text() == '' or self.line10.text() == '' or self.line11.text() == '' \
              or self.line12.text() == '' or self.line13.text() == '':
            msg1 = QMessageBox(self)
            self.messageBox = msg1
            msg1.setText('please full the blank!')
            msg1.setWindowTitle('Alert')
            msg1.resize(600, 400)
            # print('came oweeeer')
            msg1.show()
      elif (self.line.text() !='1' and  self.line.text() !='2' and self.line.text() !='3') or ( self.line2.text() !='1' and\
        self.line2.text() != '2' and self.line2.text() !='3') or (self.line3.text() !='1' and self.line3.text() !='2' and self.line3.text() !='3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (self.line4.text() !='1' and  self.line4.text() !='2' and self.line4.text() !='3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (self.line5.text() !='1' and  self.line5.text() !='2' and self.line5.text() !='3' and self.line5.text() !='4'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (self.line6.text() != '0' and self.line6.text() !='1' and  self.line6.text() !='2' and self.line6.text() !='3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (self.line7.text() != '0' and self.line7.text() != '1' and self.line7.text() != '2' and self.line7.text() != '3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (self.line8.text() != '0' and self.line8.text() != '1' and self.line8.text() != '2' and self.line8.text() != '3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (self.line9.text() != '0' and self.line9.text() != '1' and self.line9.text() != '2' and self.line9.text() != '3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (self.line10.text() != '0' and self.line10.text() != '1' and self.line10.text() != '2' and self.line10.text() != '3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (self.line11.text() != '0' and self.line11.text() != '1' and self.line11.text() != '2' and self.line11.text() != '3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (self.line12.text() != '0' and self.line12.text() != '1' and self.line12.text() != '2' and self.line12.text() != '3'):
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please enter right numbers!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
      elif (self.line13.text() != '0' and self.line13.text() != '1' and self.line13.text() != '2' and self.line13.text() != '3'):
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
        numb10 = self.line10.text()
        numb11 = self.line11.text()
        numb12 = self.line12.text()
        numb13 = self.line13.text()
        avg = ( int(numb)*4 + int(numb2) + int(numb3)*2 + int(numb4)*4 +int(numb5)*2 + int(numb6)*4 + int(numb7)*2 + int(numb8)*2+int(numb9)*1 + int(numb10)*1+
               int(numb11)*2 + int(numb12)*2 + int(numb13)*2 ) / 29

        avg = format(avg, '.2f')
        avg = 'total score is '+ str(avg)
        #print(self.path)
        try:
          file = open(self.path, "a+")
          file.write("general "+avg + "\n")
          file.close()
        except:
            print('there is no such a path')
       # print(avg,'is sum. ')
        msg = QMessageBox(self)
        self.messageBox = msg
        msg.setText(avg)
        msg.setWindowTitle('Score')

        msg.show()
        self.hide()

        self.noscoractive = False
        if self.ItOpen == 1:
            print('counter_is_it:',self.counter)
            self.myit = It(self.activevar, self.path, self.myar, op1, op2, op3, op4, self.counter)
            self.myit.show()
        else:
            print('counter_is_it:', self.counter)
            self.main3 = Market(self.activevar, op1, op2, op3, op4, self.path, self.counter,self.myar)
            self.main3.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    array = ['1','گگ','نیا','False','SEle','ls','sd']
    main11 =General(False,False,False,False,'C:/Users/win_10/Desktop/elahe-proj/final_tansa/data' +'/' +'pagetotal_'+'1'+ '.txt', 2,array)
    main11.show()
    sys.exit(app.exec_())