
import sys

from PyQt5.QtWidgets import ( QPushButton)
from PyQt5.QtWidgets import QWidget, QDesktopWidget

from firstPageSgow import FirstPageShow
from PyQt5 import  QtGui, QtCore

from PyQt5.QtWidgets import  QLabel,QVBoxLayout, QHBoxLayout, QSizePolicy
import os
class Show_need(QWidget):
    def __init__(self,path_id, parent=None):
        super(Show_need, self).__init__(parent)
        print('this is SHOW_NEED')
        self.checks()

        # self.setFont(QtGui.QFont('Arial', 12))
        self.mainLayout = QHBoxLayout()
        self.firstVertical = QVBoxLayout()
        self.secondVertical = QVBoxLayout()

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))

        myscreen = QDesktopWidget().screenGeometry()

        mywidth = myscreen.width() * 40 / 100
        myheight = myscreen.height() * 50 / 100
        self.setMinimumSize(int(mywidth), int(myheight))


        self.setFont(QtGui.QFont('Arial', 12))
        self.center1()
        self.path_need = path_id
        self.setWindowTitle(self.path_need)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))

        self.path = 'data/' +'pagetotal_'+ self.path_need.split('\n')[0] + '.txt'
        self.passPath = 'data/' + 'page1_'+self.path_need.split('\n')[0] + '.txt'
        #print('opennn',self.path)
        self.file = open(self.path, 'r')
       # print('please open file')
        self.line = self.file.readlines()
        #print('file open')
        self.file.close()
        self.my_array = []
        fix = 20
        for i in range(len(self.line)):
            self.my_array.append(QLabel(self))
            self.my_array[i].setText(self.line[i])
            self.my_array[i].resize(1000,30)
            fix += 50
            self.my_array[i].move(20,fix)
            self.my_array[i].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.secondVertical.addWidget(self.my_array[i])


        self.pb = QPushButton('ok', self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(self.button_click1)

        self.pb.move(280, 200)
       # self.pb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pb.resize(100, 40)
        self.secondVertical.addWidget(self.pb)

        self.mainLayout.addLayout(self.secondVertical)

        self.mainLayout.addLayout(self.firstVertical)

        self.setLayout(self.mainLayout)

    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)

    def center1(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        #print(self.size(),'size')

    def button_click1(self):

       print('yes come')
       self.hide()
       #self.firstapage = FirstPage(self.passPath)
       self.firstPage = FirstPageShow(self.passPath)
       self.firstPage.show()





