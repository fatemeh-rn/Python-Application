import time

from PyQt5.QtWidgets import (QPushButton,
                             QLineEdit, QMessageBox, QSizePolicy)
from PyQt5.QtWidgets import  QLabel,QVBoxLayout,QHBoxLayout
from PyQt5.QtWidgets import QWidget, QDesktopWidget

from general import General
from sorry_page import Sorry_page
from PyQt5 import  QtGui, QtCore
import os

class PrimaryFiltering(QWidget):
    def __init__(self,op1, op2, op3,op4,path, counter,first_ary, parent=None):
        super(PrimaryFiltering, self).__init__(parent)
        self.checks()
        print('in promatu filtering')
        self.setFont(QtGui.QFont('B Nazanin', 12))

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))
        print('gggggggggggggg')
        self.mainLayout = QHBoxLayout()
        self.mysize = self.frameGeometry().size()
        self.myscreen = QDesktopWidget().screenGeometry()

        self.path = path
        self.mywidth = 300
        self.myheight = 200

        self.setMinimumSize(int(self.mywidth), int(self.myheight))

        self.center()
        self.setWindowTitle('primary filtering')
        self.myar = first_ary
       # print('phycheck,')
        print('we came there filter primary show')
        self.firstVertical = QVBoxLayout()
        self.path = path
        self.counter = counter
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('If need is repetitive:')
        self.nameLabel.move(int(self.mywidth/1.7), int(self.myheight/13.5))
        self.nameLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel)
       # self.nameLabel.resize(self.mywidth/10, self.myheight/10)

        self.seconeVertical = QVBoxLayout()
        self.line = QLineEdit(self)
        self.line.move(int(self.mywidth/1.9), int(self.myheight/13.5))#300,20
        self.line.resize(int(self.mywidth/23), int(self.myheight/10.8))#25, 25)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.seconeVertical.addWidget(self.line)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('If need is related to field of medicine')
        self.nameLabel2.move(int(self.mywidth/1.7), int(self.myheight/4.5))#340, 60)
        self.nameLabel2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel2)

        self.line2 = QLineEdit(self)
        self.line2.move(int(self.mywidth/1.9) , int(self.myheight/4))#300, 60)
        self.line2.resize(int(self.mywidth/40), int(self.myheight/10.8))#25, 25)
        self.line2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.seconeVertical.addWidget(self.line2)

        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('if need is related to field of IT')
        self.nameLabel3.move(int(self.mywidth / 1.7), int(self.myheight / 2.7))
        self.nameLabel3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel3)

        self.line3 = QLineEdit(self)
        self.line3.move(int(self.mywidth/1.9), int(self.myheight/2.7))#300, 100)
        self.line3.resize(int(self.mywidth/23), int(self.myheight/10.8))#25, 25)
        self.line3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.seconeVertical.addWidget(self.line3)

        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('If area of need is not clear')
        self.nameLabel4.move(int(self.mywidth / 1.7), int(self.myheight / 1.9))  # 340, 140)
        self.nameLabel4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel4)

        self.line4 = QLineEdit(self)
        self.line4.move(int(self.mywidth/1.9), int(self.myheight/1.9))#300, 140)
        self.line4.resize(int(self.mywidth/23), int(self.myheight/10.8))#25, 25)
        self.line4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.seconeVertical.addWidget(self.line4)


        self.nameLabel5 = QLabel(self)
        self.nameLabel5.setText('If the field of demand is not defined')
        self.nameLabel5.move(int(self.mywidth / 1.7), int(self.myheight / 1.5))  # 340, 180)
        self.nameLabel5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel5)

        self.line5 = QLineEdit(self)
        self.line5.move(int(self.mywidth/1.9), int(self.myheight/1.5))#300, 180)
        self.line5.resize(int(self.mywidth/23), int(self.myheight/10.8))#25, 25)
        self.line5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.seconeVertical.addWidget(self.line5)


        self.nameLabel6 = QLabel(self)
        self.nameLabel6.setText('If moral principles are not observed')
        self.nameLabel6.move(int(self.mywidth/1.7), int(self.myheight/1.3 ))#340, 220)
        self.nameLabel6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel6)

        self.line6 = QLineEdit(self)
        self.line6.move(int(self.mywidth/1.9), int(self.myheight/1.3))#300, 220)
        self.line6.resize(int(self.mywidth/23), int(self.myheight/10.8))#25, 25))
        self.line6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.seconeVertical.addWidget(self.line6)

        self.thirdvertical = QVBoxLayout()

        self.nameLabel16 = QLabel(self)
        #self.nameLabel16.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel16.setText('Not delete:1')
        self.nameLabel16.move(int(self.mywidth/5.8), int(self.myheight/2.7))#100, 100)
        self.nameLabel16.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdvertical.addWidget(self.nameLabel16)

        self.nameLabel7 = QLabel(self)
        #self.nameLabel7.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel7.setText('Delete:0 ')
        self.nameLabel7.move(int(self.mywidth/5.8), int(self.myheight/2))#100, 130)
        self.nameLabel7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdvertical.addWidget(self.nameLabel7)

        self.thirdvertical.addStretch(1)

        self.nameLabel8 = QLabel(self)
        #self.nameLabel8.setText('حذف کردsdsfsdfن: 0 ')
        self.nameLabel8.move(int(self.mywidth/1.7), int(self.myheight/1.2))#100, 130)
        self.nameLabel8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel8)

        self.pb1 = QPushButton('ok', self)
        self.pb1.setStyleSheet("background-color: White")
        self.pb1.clicked.connect(lambda: self.button_click2(op1, op2, op3, op4))
        self.pb1.resize(int(self.mywidth/5.8),int(self.myheight/6.7))#100, 40)
        self.pb1.move(int(self.mywidth/2), int(self.myheight/1.05))#290, 260)
        self.pb1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.seconeVertical.addWidget(self.pb1)

        self.selffourthvertic = QVBoxLayout()

        self.mainLayout.addLayout(self.thirdvertical)
        self.mainLayout.addLayout(self.seconeVertical)
        self.mainLayout.addLayout(self.selffourthvertic)
        self.mainLayout.addLayout(self.firstVertical)

        print('uCanChange')
        self.setLayout(self.mainLayout)

    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)

    def center(self):
        print('sscenterr')
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        #print(self.size(), 'size')

    # noinspection PyTypeChecker
    def button_click2(self,op1, op2, op3, op4):
     print('i m here in ok primary')

     if self.line.text() == '' or self.line2.text() == '' or self.line3.text() == '' or self.line4.text() == '' or self.line5.text() == '' or self.line6.text() == '':
          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please full the blank!')
          msg1.setWindowTitle('Alert')
          msg1.resize(600, 400)
          # print('came oweeeer')
          msg1.show()
     elif (self.line.text() !='0' and  self.line.text() !='1') or (self.line2.text() !='0' and self.line2.text() !='1')\
       or (self.line3.text() != '0' and self.line3.text() !='1') or (self.line4.text() !='0' and self.line4.text() !='1') or (self.line5.text() !='0' and self.line5.text() !='1')\
             or (self.line6.text() != '0' and self.line6.text() !='1') :

          msg1 = QMessageBox(self)
          self.messageBox = msg1
          msg1.setText('please insert 0 or 1!')
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
        
        self.ItWouldOpen = 0
        self.noscoractive = False
        self.hide()

        if int(numb3) == 1:
            if int(numb) == 0 or int(numb2) == 0 or int(numb6) == 0 or int(numb4) == 0 or int(numb5) == 0:
                msg31 = QMessageBox(self)
                self.messageBox = msg31
                msg31.setWindowTitle('Invalid Need !')
                msg31.setText(
                    "need will be deleted  \n\n "
                    )
                msg31.resize(600, 400)
                msg31.show()
                #time.sleep(3)


                print('counter_is_primary:',self.counter)
                self.noscoractive = True
                self.mymessage = Sorry_page(self.noscoractive,self.path, self.myar)
               # self.mymessage.show()
            else:
                self.general_main = General(self.noscoractive, op1, op2, op3, op4, self.path, self.counter, self.myar,
                                            self.ItWouldOpen)
                self.general_main.show()

        else:
            print('counter_is_primary:', self.counter)
            self.ItWouldOpen = 1
            self.general_main = General(self.noscoractive,op1, op2, op3, op4, self.path , self.counter,self.myar, self.ItWouldOpen)
            self.general_main.show()

