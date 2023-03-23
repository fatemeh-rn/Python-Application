
import os
from PyQt5.QtWidgets import ( QPushButton, QLineEdit, QMessageBox)
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QGridLayout, QSizePolicy
from PyQt5 import QtCore, QtGui
from manager import Window
import end
import time

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

class Welcome(QWidget):
    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent)
        self.checks()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))
        print('in welcome')


        self.layoutGrid = QGridLayout()
        self.setLayout(self.layoutGrid)

        myscreen = QDesktopWidget().screenGeometry()
        mywidth = myscreen.width() * 60 / 100
        myheight = myscreen.height() * 20/ 100
        self.setMinimumSize(int(mywidth), int(myheight))
        #print(mywidth, myheight, 'sdfsdf', myscreen.width(), myscreen.height())
        self.center()
        self.setFont(QtGui.QFont('Arial', 12))
        self.setWindowTitle('Wellcome !')

        print('in wellcome tfor test')

        self.nameLabel = QLabel(self)
        self.nameLabel.setStyleSheet( "color: black;")#"color: red;")
        #self.nameLabel.setFont(QtGui.QFont('Arial', 10))
        self.nameLabel.setText('Please Enter Your Partner: ')
        #self.nameLabel.resize(100,200)
       # self.nameLabel.move(140, 100)
        self.layoutGrid.addWidget(self.nameLabel)

        self.line = QLineEdit(self)
        # self.line.move(mywidth*)#300, 100)
        # self.line.resize(300, 32)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layoutGrid.addWidget(self.line)

        self.pb = QPushButton('continue', self)
        self.pb.clicked.connect(self.button_click1)
        self.pb.setStyleSheet("background-color: White")
        self.pb.resize(int(mywidth/200), int(myheight/50) )#100, 40)

        self.pb1 = QPushButton('show results', self)
        self.pb1.clicked.connect(self.button_click2)
        self.pb1.setStyleSheet("background-color: White")
        self.pb1.resize(int(mywidth / 200), int(myheight / 50))  # 100, 40)

        # self.pb.move(280, 200)
        # self.line.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.layoutGrid.addWidget(self.pb)
        self.layoutGrid.addWidget(self.pb1)

        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setFont(QtGui.QFont('Arial', 9))
        self.nameLabel1.setText('NOTE: please insert names in english and seprate them by comma ')
        # self.nameLabel1.move(680, 90)
        # self.nameLabel1.resize(250, 50)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layoutGrid.addWidget(self.nameLabel1)

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        # print(self.size(),'size')
#self.my_line_edit.setStyleSheet("color: rgb(255, 0, 0);")
    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)#darkCyan
        self.setPalette(p)

    def button_click2(self):
        if not os.path.exists("./data"):
            print('sdfsdfsdfsdf')

            self.msg10 = QMessageBox(self)
            self.messageBox = self.msg10
            self.msg10.setText(' \n no record to preview \n')
            self.msg10.setWindowTitle('Alert')
            self.msg10.resize(1000, 800)
            self.msg10.exec_()
            time.sleep(2)
           # self.hide()
        else:
            self.hide()
            self.mainEnd = end.End(False, [], "./data")#final_tansa.end.End(False, [], "./data")#add_scrol()  #1447e, [], "./data")001423.1456987/*
            self.mainEnd.show()

    def button_click1(self):
        #print('i m here in ok')
        if self.line.text() == '':
            msg1 = QMessageBox(self)
            self.messageBox = msg1
            msg1.setText('please full the blank!')
            msg1.setWindowTitle('Alert')
            msg1.resize(600, 400)
            #print('came oweeeer')
            msg1.show()

        else:
            numb = self.line.text()
            # print(numb)

            self.hide()
            createFolder('./data')
            self.main11 = Window(numb, "./data")
            self.main11.show()


