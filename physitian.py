
import sys
from PyQt5.QtWidgets import (QApplication,  QPushButton,
                             QLineEdit,  QMessageBox
                             )
from PyQt5.QtWidgets import  QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtWidgets import  QWidget, QDesktopWidget

from equipment import Equipment
from facilities import Facilities
from patient import Patient
from end import End

from PyQt5 import  QtGui, QtCore
import os

class Physiacan(QWidget):
    def __init__(self ,activevar,op2, op3, op4, path, counter,first_aray, parent=None):
        super(Physiacan, self).__init__(parent)
        self.checks()
       # self.setFont(QtGui.QFont('Arial', 12))
        self.setFont(QtGui.QFont('B Nazanin', 12))
        self.mainLayout = QHBoxLayout()
        self.firstVertical = QVBoxLayout()
        self.secondVertical = QVBoxLayout()
        self.thirdVetical = QVBoxLayout()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))

        myscreen = QDesktopWidget().screenGeometry()

        mywidth = myscreen.width() * 30 / 100
        myheight = myscreen.height() * 25 / 100
        self.setMinimumSize(int(mywidth), int(myheight))
        self.center()
        #print(counter,'counter')
        #mai = Window()
        self.path = path
        self.counter = counter
        self.myar = first_aray
        self.activevar = activevar
        self.setWindowTitle('physican')

        #print('we came there physican')
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Impact of need satisfaction on better performance ')
        self.line = QLineEdit(self)
        self.line.move(300, 20)
        self.line.resize(25, 25)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line)
        self.nameLabel.move(340, 20)
        self.nameLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Impact of need satisfaction on credit of physician ')
        self.line2 = QLineEdit(self)
        self.line2.move(300, 60)
        self.line2.resize(25, 25)
        self.line2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line2)
        self.nameLabel2.move(340, 60)
        self.nameLabel2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel2)


        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Impact of need satisfaction on reducing risks associated with health ')
        self.line3 = QLineEdit(self)
        self.line3.move(300, 100)
        self.line3.resize(25, 25)
        self.line3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line3)
        self.nameLabel3.move(340, 100)
        self.nameLabel3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel3)

        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('Impact of need satisfaction on amount of risk-taking and financial benefit of possible new ways in the field of needs')
        self.line4 = QLineEdit(self)
        self.line4.move(300, 140)
        self.line4.resize(25, 25)
        self.line4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line4)
        self.nameLabel4.move(340, 140)
        self.nameLabel4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel4)

        self.nameLabel5 = QLabel(self)
        self.nameLabel5.setText('Impact of need satisfaction on increasing financial profit')
        self.line5 = QLineEdit(self)
        self.line5.move(300, 180)
        self.line5.resize(25, 25)
        self.line5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line5)
        self.nameLabel5.move(340, 180)
        self.nameLabel5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel5)

        self.nameLabel115 = QLabel(self)
        self.nameLabel115.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel115)

        self.nameLabel55 = QLabel(self)
        self.nameLabel55.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel55.setText('None -> 0')
        self.nameLabel55.move(100, 120)
        self.nameLabel55.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel55)

        self.nameLabel56 = QLabel(self)
        self.nameLabel56.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel56.setText('low -> 1')
        self.nameLabel56.move(100, 135)
        self.nameLabel56.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel56)

        self.nameLabel57 = QLabel(self)
        self.nameLabel57.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel57.setText('medium -> 2')
        self.nameLabel57.move(100, 150)
        self.nameLabel57.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel57)

        self.nameLabel58 = QLabel(self)
        self.nameLabel58.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel58.setText('high -> 3')
        self.nameLabel58.move(100, 165)
        self.nameLabel58.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel58)

    
        self.pb = QPushButton('ok', self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(lambda :self.button_click1(op2, op3, op4))
        self.pb.resize(100, 40)
        self.pb.move(280, 220)
        self.pb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.pb)

        self.thirdVetical.addStretch(5)

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
    def button_click1(self, op2, op3, op4):
     #print('i m here in ok')
     if self.line.text() == '' or self.line2.text() == '' or self.line3.text() == '' or self.line4.text() == '' or self.line5.text() == '':
            msg1 = QMessageBox(self)
            self.messageBox = msg1
            msg1.setText('please full the blank!')
            msg1.setWindowTitle('Alert')
            msg1.resize(600, 400)
            # print('came oweeeer')
            msg1.show()
     elif (self.line.text() != '1' and self.line.text() != '2' and self.line.text() != '3' and self.line.text() != '0'):
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
     else:
        numb = self.line.text()
        numb2 = self.line2.text()
        numb3 = self.line3.text()
        numb4 = self.line4.text()
        numb5 = self.line5.text()
       # print(numb,numb4,numb2,numb3,'get numb')
        #print(type(int(numb3)),'my type')
        avg = (int(numb)*2 + int(numb2)*2 + int(numb3)*2 + int(numb4)*4 +int(numb5)*2) / 12
        avg = format(avg, '.2f')
        avg = 'total score is '+ str(avg)
        file = open(self.path,"a")
        file.write("physitian "+avg + "\n")
        file.close()
        #print(avg,'is sum. ')
        msg = QMessageBox(self)
        self.messageBox = msg
        msg.setText(avg)
        msg.setWindowTitle('Score')
        msg.resize(600,400)

        msg.show()
        self.hide()
        # self.mai = Window()
        # print(self.mai.phycheck,'yesssssssssssssssssssss')

        #
        self.counter -= 1
        print('count',self.counter)
        if self.counter == 0:
            print('come to if end physic')
            self.end_page = End(self.activevar,self.myar, self.path)
            self.end_page.show()
        else:
            if op2 == True  :

                self.main3 = Patient(self.activevar, op3, op4, self.path, self.counter,self.myar)
                self.main3.show()
            elif op3 == True  :
         #       print('her e in facilites')
                self.main4 = Facilities(self.activevar, op4, self.path, self.counter, self.myar)
                self.main4.show()
            elif op4 == True  :

                self.main5 = Equipment(self.activevar, self.path, self.counter,self.myar)
                self.main5.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    array = ['1','گگ','نیا','False','False','False','SEle','ls','sd']
    main11 =Physiacan(False,False,False,False, 'data' +'/' +'pagetotal_'+'5'+ '.txt', 2,array)
    main11.show()
    sys.exit(app.exec_())