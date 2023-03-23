
from PyQt5.QtWidgets import ( QPushButton,
                             QLineEdit,  QMessageBox
                             )
from PyQt5.QtWidgets import  QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtWidgets import  QWidget, QDesktopWidget

from end import End
from facilities import Facilities
from equipment import Equipment
from PyQt5 import  QtGui, QtCore
import os

class Patient(QWidget):
    def __init__(self,activevar, op3, op4, path, counter, first_aray, parent=None):
        super(Patient, self).__init__(parent)
        self.checks()
        #self.setFont(QtGui.QFont('Arial', 12))
        self.setFont(QtGui.QFont('B Nazanin', 12))
        self.mainLayout = QHBoxLayout()
        self.firstVertical = QVBoxLayout()
        self.secondVertical = QVBoxLayout()
        self.thirdVetical = QVBoxLayout()
        self.fourthVertical = QVBoxLayout()
        self.fifthVertical = QVBoxLayout()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))

        myscreen = QDesktopWidget().screenGeometry()

        mywidth = myscreen.width() * 70 / 100
        myheight = myscreen.height() * 35 / 100
        self.setMinimumSize(int(mywidth), int(myheight))
        self.center()
        print('this is patient')

        self.setWindowTitle('patient')
        self.path = path
        self.counter = counter
        self.myar = first_aray
        self.activevar = activevar
        #print('we came there patient')
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Effect of disease related to need area in quality of life ')
        self.line = QLineEdit(self)
        self.line.move(300, 20)
        self.line.resize(25, 25)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line)
        self.nameLabel.move(340, 20)
        self.nameLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('The risk of possible new ways associated with health ')
        self.line2 = QLineEdit(self)
        self.line2.move(300, 60)
        self.line2.resize(25, 25)
        self.line2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line2)
        self.nameLabel2.move(340, 60)
        self.nameLabel2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel2)

        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Amount of disease prevalence involved in need area ')
        self.line3 = QLineEdit(self)
        self.line3.move(300, 100)
        self.line3.resize(25, 25)
        self.line3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line3)
        self.nameLabel3.move(340, 100)
        self.nameLabel3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel3)

        print('sdfsdfsdfsd')
        self.nameLabel55 = QLabel(self)
        self.nameLabel55.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel55.setText('سوالات 1 تا 3: ')
        self.nameLabel55.move(2, 51)
        self.nameLabel55.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel55)

        self.nameLabel551 = QLabel(self)
        self.nameLabel551.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel551.setText('هیچکدام->0')
        self.nameLabel551.move(100, 30)
        self.nameLabel551.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel551)

        self.nameLabel56 = QLabel(self)
        self.nameLabel56.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel56.setText('کم->1')
        self.nameLabel56.move(100, 45)
        self.nameLabel56.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel56)

        self.nameLabel57 = QLabel(self)
        self.nameLabel57.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel57.setText('متوسط->2')
        self.nameLabel57.move(100, 60)
        self.nameLabel57.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel57)

        self.nameLabel58 = QLabel(self)
        self.nameLabel58.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel58.setText('زیاد->3')
        self.nameLabel58.move(100, 75)
        self.nameLabel58.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.thirdVetical.addWidget(self.nameLabel58)

        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('Effect of possible new therapies involved need area on quality of life ')
        self.line4 = QLineEdit(self)
        self.line4.move(300, 140)
        self.line4.resize(25, 25)
        self.line4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line4)
        self.nameLabel4.move(340, 140)
        self.nameLabel4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel4)

        self.nameLabel555 = QLabel(self)
        self.nameLabel55.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel555.setText('سوال 4 : ')
        self.nameLabel555.move(20, 135)
        self.nameLabel555.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fourthVertical.addWidget(self.nameLabel555)

        self.nameLabel525 = QLabel(self)
        self.nameLabel525.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel525.setText('مرتبط با مرگ و میر->2')
        self.nameLabel525.move(100, 120)
        self.nameLabel525.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fourthVertical.addWidget(self.nameLabel525)

        self.nameLabel535 = QLabel(self)
        self.nameLabel535.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel535.setText('  مرتبط با نارضایتی->1')
        self.nameLabel535.move(100, 135)
        self.nameLabel535.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fourthVertical.addWidget(self.nameLabel535)

        self.nameLabel545 = QLabel(self)
        self.nameLabel545.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel545.setText('  ترکیب دو مورد بالا->0')
        self.nameLabel545.move(100, 150)
        self.nameLabel545.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fourthVertical.addWidget(self.nameLabel545)

        self.nameLabel5 = QLabel(self)
        self.nameLabel5.setText('Obvious or hidden disease ')
        self.line5 = QLineEdit(self)
        self.line5.move(300, 190)
        self.line5.resize(25, 25)
        self.line5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.line5)
        self.nameLabel5.move(340, 190)
        self.nameLabel5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel5)
        print('before lablee')

        self.nameLabel1115 = QLabel(self)
        self.nameLabel1115.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.firstVertical.addWidget(self.nameLabel1115)
        print('after lableee')
        self.nameLabel745 = QLabel(self)
        self.nameLabel745.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel745.setText(' سوال 5 :')
        self.nameLabel745.move(20, 191)
        self.nameLabel745.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel745)
        print('before penhan')
        self.nameLabel625 = QLabel(self)
        self.nameLabel625.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel625.setText('پنهان->1')
        self.nameLabel625.move(100, 185)
        self.nameLabel625.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel625)

        self.nameLabel635 = QLabel(self)
        self.nameLabel635.setFont(QtGui.QFont('B Nazanin', 10))
        self.nameLabel635.setText('آشکار->2   ')
        self.nameLabel635.move(100, 200)
        self.nameLabel635.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fifthVertical.addWidget(self.nameLabel635)



        self.pb = QPushButton('ok', self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(lambda: self.button_click1(op3, op4))
        self.pb.resize(100, 40)
        self.pb.move(280, 220)
        self.pb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.secondVertical.addWidget(self.pb)

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
        print(self.size(),'size')

    # noinspection PyTypeChecker
    def button_click1(self,op3, op4):
     #print('i m here in ok')
     if self.line.text() == '' or self.line2.text() == '' or self.line3.text() == '' or self.line4.text() == '' or self.line5.text() == '':
         msg1 = QMessageBox(self)
         self.messageBox = msg1
         msg1.setText('please full the blank!')
         msg1.setWindowTitle('Alert')
         msg1.resize(600, 400)
      #   print('came oweeeer non')
         msg1.show()
     elif (self.line.text() != '1' and self.line.text() != '2' and self.line.text() != '3' and self.line.text() != '0'):
         msg1 = QMessageBox(self)
         self.messageBox = msg1
         msg1.setText('please enter right numbers!')
         msg1.setWindowTitle('Alert')
         msg1.resize(600, 400)
       #  print('came oweeeer 1')
         msg1.show()
     elif (
             self.line2.text() != '1' and self.line2.text() != '2' and self.line2.text() != '3' and self.line2.text() != '0'):
         msg1 = QMessageBox(self)
         self.messageBox = msg1
         msg1.setText('please enter right numbers!')
         msg1.setWindowTitle('Alert')
         msg1.resize(600, 400)
        # print('came oweeeer 2')
         msg1.show()
     elif (
             self.line3.text() != '1' and self.line3.text() != '2' and self.line3.text() != '3' and self.line3.text() != '0'):
         msg1 = QMessageBox(self)
         self.messageBox = msg1
         msg1.setText('please enter right numbers!')
         msg1.setWindowTitle('Alert')
         msg1.resize(600, 400)
         #print('came oweeeer 3')
         msg1.show()
     elif (self.line4.text() != '1' and self.line4.text() != '2' and self.line4.text() != '3'):
         msg1 = QMessageBox(self)
         self.messageBox = msg1
         msg1.setText('please enter right numbers!')
         msg1.setWindowTitle('Alert')
         msg1.resize(600, 400)
         #print('came oweeeer 4')
         msg1.show()
     elif (self.line5.text() != '2' and self.line5.text() != '1'):
         msg1 = QMessageBox(self)
         self.messageBox = msg1
         msg1.setText('please enter right numbers!')
         msg1.setWindowTitle('Alert')
         msg1.resize(600, 400)
         #print('came oweeeer 5')
         msg1.show()
     else:
        #print('came in number gove')
        numb = self.line.text()
        numb2 = self.line2.text()
        numb3 = self.line3.text()
        numb4 = self.line4.text()
        numb5 = self.line5.text()
        avg = (int(numb)*2 + int(numb2)*4 + int(numb3)*2 + int(numb4)*4 + int(numb5)*2) / 14
        avg = format(avg, '.2f')
        avg = 'total score is '+ str(avg)
        file = open(self.path, "a")
        file.write("patient " + avg + "\n")
        file.close()
        #print(avg,'is sum. ')
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
        else:
            if op3 == True:
                self.main4 = Facilities(self.activevar, op4, self.path, self.counter, self.myar)
                self.main4.show()
            elif op4 == True:
                self.main5 = Equipment(self.activevar, self.path, self.counter, self.myar)
                self.main5.show()
