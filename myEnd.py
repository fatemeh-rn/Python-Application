
from PyQt5.QtGui import  QPalette
from PyQt5.QtWidgets import ( QCheckBox,  QGroupBox,
                              QPushButton,  QHBoxLayout)
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import  QWidget, QDesktopWidget

from Show_need import Show_need
from PyQt5 import  QtGui, QtCore
import os

class End(QWidget):
    def __init__(self, path_need, parent=None):
        super(End, self).__init__(parent)
        print('this is myend')
        self.checks()
        self.setFont(QtGui.QFont('Arial', 12))
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))
        self.path = "C:/Users/win_10/Desktop/elahe-proj/final_tansa/data/total.txt"
        self.center()
        self.setWindowTitle('Show Scores')
       # print('here in end')
        file = open(path_need, "r")
        lines1 = file.readlines()
        file.close()
        #print(lines1,'liness1',self.path,'my_path',path_need)
        avg = 0.0
        line_number = 0
        for line in lines1:
            avg += float(line.split(" ")[4])
            line_number += 1

        avg = float(avg/line_number)
        avg = format(avg, '.2f')
        total_file = open(self.path, "a")
        total_file.write(path_need.split("/")[len(path_need.split("/"))-1].split(".")[0] + " " + str(avg) + "\n")
        total_file.close()
        self.center()
        self.setWindowTitle('Show Scores')
        #print('we came there filter')
        #self.path = path_need
        self.my_need = []
        self.my_avg = []
        need = []
        avg = []
       # print('heree1')
        total_file = open(self.path, "r")
        lines = total_file.readlines()
        total_file.close()
        #print('line',lines)
        for line in lines:
            need.append(line.split(" ")[0])
            #print('lllll: ',line.split(" ")[1])
            avg.append(float(line.split(" ")[1]))
        #print(avg,' :avg: ',need)
        self.need_avg = self.bubbleSort(avg, need)
        self.array_width = 50

        for i in range(len(self.need_avg[0])):

            self.my_need.append(QCheckBox( self.need_avg[0][i],self))

            self.my_need[i].setChecked(False)
            self.my_need[i].resize(100,100)
            self.my_avg.append(QLabel(str(self.need_avg[1][i]),self))
            self.my_avg[i].setText(str(self.need_avg[1][i]))
            self.array_width += 100
            self.my_need[i].move(20, self.array_width)
            self.my_avg[i].move(260, self.array_width)

        self.pb = QPushButton('ok', self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(self.button_click)
        self.pb.resize(50, 50)
        self.pb.move(340, 200)

    def sliderval(self):
     #   print(self.s1.value())
        palette = QPalette()
        self.l1.setPalette(palette)

    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)


    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def button_click(self):

        for i in range(len(self.need_avg[0])):
            #print(self.my_need[i].isChecked())
            if self.my_need[i].isChecked() == True:
                self.show_need = Show_need(self.need_avg[0][i])
                self.show_need.show()
            
    def createHorizontalLayout(self):
     self.horizontalGroupBox = QGroupBox("What is your favorite color?")
     self.horizontalGroupBox.move(500,500)
     layout = QHBoxLayout()

     buttonBlue = QPushButton('Blue', self)
     #buttonBlue.clicked.connect(self.on_click)
     layout.addWidget(buttonBlue)


    def bubbleSort(self,alist, al):

        list = []
        for passnum in range(len(alist) - 1, 0, -1):
            for i in range(passnum):
                if alist[i] > alist[i + 1]:
                    temp = alist[i]
                    alist[i] = alist[i + 1]
                    alist[i + 1] = temp
                    temp1 = al[i]
                    al[i] = al[i + 1]
                    al[i + 1] = temp1
        list.append(al)
        list.append(alist)
        return list
