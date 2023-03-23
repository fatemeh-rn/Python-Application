
import sys
from PyQt5.QtWidgets import (QApplication,
                              QPushButton,
                             QLineEdit,   QMessageBox
                             )
from PyQt5.QtWidgets import  QLabel,QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtWidgets import  QWidget, QDesktopWidget

from physitian import Physiacan
from patient import Patient
from facilities import Facilities
from equipment import Equipment
from PyQt5 import  QtGui, QtCore
import os
from end import End

class Market(QWidget):
    def __init__(self,activevar, op1, op2, op3,op4 ,path ,counter,first_ary, parent=None):
        super(Market, self).__init__(parent)
        self.checks()
        #self.setFont(QtGui.QFont('Arial', 12))
        self.setFont(QtGui.QFont('B Nazanin', 12))
        self.mainLayout = QHBoxLayout()
        self.firstVertical = QVBoxLayout()
        self.secondVertical = QVBoxLayout()
        self.thirdVetical = QVBoxLayout()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))

        myscreen = QDesktopWidget().screenGeometry()

        mywidth = myscreen.width() * 40 / 100
        myheight = myscreen.height() * 55 / 100
        self.setMinimumSize(int(mywidth), int(myheight))

        self.center()
        #mai = Window()
        self.path = path
        self.counter = counter
        self.myar = first_ary
        self.activevar = activevar
        self.setWindowTitle('market')

        #print('we came there market')
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Amount of need market share ')
        self.nameLabel.move(340, 20)
        self.nameLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel)
        self.line = QLineEdit(self)
        self.line.move(300, 20)
        self.line.resize(25, 25)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line)


        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Market growth rate in relevant field of need ')
        self.line2 = QLineEdit(self)
        self.line2.move(300, 60)
        self.line2.resize(25, 25)
        self.line2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line2)
        self.nameLabel2.move(340, 60)
        self.nameLabel2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel2)

        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Amount of ability for need solution to enter market and compete with antagonist in market ')
        self.line3 = QLineEdit(self)
        self.line3.move(300, 100)
        self.line3.resize(25, 25)
        self.line3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line3)
        self.nameLabel3.move(340, 100)
        self.nameLabel3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel3)

        self.nameLabel55 = QLabel(self)
        self.nameLabel55.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel55.setText('None -> 0')
        self.nameLabel55.move(100, 140)
        self.nameLabel55.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel55)

        self.nameLabel56 = QLabel(self)
        self.nameLabel56.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel56.setText('low -> 1')
        self.nameLabel56.move(100, 155)
        self.nameLabel56.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel56)

        self.nameLabel57 = QLabel(self)
        self.nameLabel57.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel57.setText('medium -> 2')
        self.nameLabel57.move(100, 170)
        self.nameLabel57.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel57)

        self.nameLabel58 = QLabel(self)
        self.nameLabel58.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel58.setText('high -> 3')
        self.nameLabel58.move(100, 185)
        self.nameLabel58.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel58)

        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('Access to investors in field of need')
        self.line4 = QLineEdit(self)
        self.line4.move(300, 140)
        self.line4.resize(25, 25)
        self.line4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line4)
        self.nameLabel4.move(340, 140)
        self.nameLabel4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel4)

        self.nameLabel5 = QLabel(self)
        self.nameLabel5.setText('Impact of need satisfaction on competition of customers in market ')
        self.line5 = QLineEdit(self)
        self.line5.move(300, 180)
        self.line5.resize(25, 25)
        self.line5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line5)
        self.nameLabel5.move(340, 180)
        self.nameLabel5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel5)

        self.nameLabel6 = QLabel(self)
        self.nameLabel6.setText('Insurance support in need area ')
        self.line6 = QLineEdit(self)
        self.line6.move(300, 220)
        self.line6.resize(25, 25)
        self.line6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line6)
        self.nameLabel6.move(340, 220)
        self.nameLabel6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel6)

        self.nameLabel7 = QLabel(self)
        self.nameLabel7.setText('Investors risk-taking ')
        self.line7 = QLineEdit(self)
        self.line7.move(300, 260)
        self.line7.resize(25, 25)
        self.line7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line7)
        self.nameLabel7.move(340, 260)
        self.nameLabel7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel7)

        self.nameLabel8 = QLabel(self)
        self.nameLabel8.setText('Solution profitability after entering the market')
        self.line8 = QLineEdit(self)
        self.line8.move(300, 300)
        self.line8.resize(25, 25)
        self.line8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line8)
        self.nameLabel8.move(340, 300)
        self.nameLabel8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel8)

        self.nameLabel9 = QLabel(self)
        self.nameLabel9.setText('Target population in market segments of need')
        self.line9 = QLineEdit(self)
        self.line9.move(300, 340)
        self.line9.resize(25, 25)
        self.line9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line9)
        self.nameLabel9.move(340, 340)
        self.nameLabel9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel9)

        self.nameLabel10 = QLabel(self)
        self.nameLabel10.setText('Appropriate relationship between cost and efficiency of need responding ')
        self.line10 = QLineEdit(self)
        self.line10.move(300, 380)
        self.line10.resize(25, 25)
        self.line10.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line10)
        self.nameLabel10.move(340, 380)
        self.nameLabel10.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel10)

        self.nameLabel11 = QLabel(self)
        self.nameLabel11.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel11)

        #print(mai.phycheck,'im window qChecksum')

        self.pb = QPushButton('ok', self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(lambda :self.button_click3(op1, op2, op3, op4))
        self.pb.resize(100, 40)
        self.pb.move(280, 420)
        self.pb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.pb)

        self.thirdVetical.addStretch(15)


        self.mainLayout.addLayout(self.thirdVetical)

        self.mainLayout.addLayout(self.secondVertical)

        self.mainLayout.addLayout(self.firstVertical)

        self.setLayout(self.mainLayout)

    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)

    def center(self):
        #print('come to senter')
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        #print(self.size(),'size')

    # noinspection PyTypeChecker
    def button_click3(self,op1, op2, op3, op4):
        #print('i m here in ok')
     if self.line.text() == '' or self.line2.text() == '' or self.line3.text() == '' or self.line4.text() == ''or self.line5.text() == '' or \
        self.line6.text() == '' or self.line7.text() == '' or self.line8.text() == '' or self.line9.text() == '' or self.line10.text() == '':
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
     elif (self.line5.text() != '1' and self.line5.text() != '2' and self.line5.text() != '3'and self.line5.text() != '0'):
         msg1 = QMessageBox(self)
         self.messageBox = msg1
         msg1.setText('please enter right numbers!')
         msg1.setWindowTitle('Alert')
         msg1.resize(600, 400)
         # print('came oweeeer')
         msg1.show()
     elif (self.line6.text() != '2' and self.line6.text() != '1'and self.line6.text() != '0' and self.line6.text() != '3'):
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
     elif (
             self.line10.text() != '2' and self.line10.text() != '1' and self.line10.text() != '0' and self.line10.text() != '3'):
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
        # print(numb,numb1,numb2,numb3)
        # print(type(int(numb3)),'my type')
        avg = (int(numb)*4 + int(numb2)*2 + int(numb3)*2 + int(numb4)*4 + int(numb5)*1 + int(numb6)*2 + int(numb7)*4 + int(numb8)*4 +
               int(numb9) * 2 + int(numb10) * 4) / 29
        avg = format(avg, '.2f')
        avg = 'total score is '+ str(avg)
        #print(avg,'is sum. ')
        file = open(self.path, "a")
        file.write("market "+avg + "\n")
        file.close()
        msg = QMessageBox(self)
        self.messageBox = msg
        msg.setText(avg)
        msg.setWindowTitle('Score')
        #msg.resize(600,400)

        msg.show()
        self.hide()
 
        if op1 == True  :

                self.main3 = Physiacan(self.activevar, op2, op3, op4, self.path, self.counter,self.myar)
                self.main3.show()
        elif op2 == True  :

                self.main4 = Patient(self.activevar, op3, op4, self.path, self.counter,self.myar)
                self.main4.show()
        elif op3 == True  :

                self.main4 = Facilities(self.activevar,op4, self.path, self.counter,self.myar)
                self.main4.show()
        elif op4 == True  :

                self.main5 = Equipment(self.activevar, self.path, self.counter,self.myar)
                self.main5.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    array = ['1','گگ','نیا','False','SEle','ls','sd']
    main11 =Market(False,False,False,False,'C:/Users/win_10/Desktop/python.proj/show_pages2/show_pages/data' +'/' +'pagetotal_'+'1'+ '.txt', 2,array)
    main11.show()
    sys.exit(app.exec_())