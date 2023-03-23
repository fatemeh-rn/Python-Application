
from sys import exit
from PyQt5.QtWidgets import  QScrollArea
from PyQt5.QtWidgets import (  QPushButton,
                             QMessageBox
                             )
from PyQt5.QtWidgets import  QWidget, QDesktopWidget
from PyQt5.QtWidgets import  QSizePolicy, QVBoxLayout
from Show_need import Show_need
from PyQt5 import  QtGui, QtCore
import os
import re
import welcome
import time



class End(QWidget):
    def __init__(self,activevar, myar,path_need, parent=None):
        super(End, self).__init__(parent)
        print('came in endd')
        self.checks()

        self.setWindowTitle('Show Scores')
        myscreen = QDesktopWidget().screenGeometry()
        mywidth = myscreen.width() * 25 / 100
        myheight = myscreen.height() * 15 / 100
        self.setMinimumSize(int(mywidth), int(myheight))

        self.setFont(QtGui.QFont('B Nazanin', 12))
        self.setFont(QtGui.QFont('Arial', 12))
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))
        self.center()
        self.setWindowTitle('Show Scores')
        self.myar = myar
        self.path = "data/total.txt"
        if len(myar) != 0:
            self.activecar = activevar
            self.path = "data/total.txt"
            self.mypatth = 'data'+'/' +'page1_'+self.myar[0]+ '.txt'#pagetotal_12
            #self.myar = myar
            with open(self.mypatth, 'w', encoding='utf-8') as f:
                f.writelines(list("%s\n" % item for item in self.myar))

            print('here in end')
            if self.activecar == True:
             lines1 = ['total score is 0.0\n']
            else:
                print('in if path need')
                file = open(path_need, "r")
                lines1 = file.readlines()
                file.close()
                avg = 0.0
                if self.activecar == True:
                    avg = -1.0
                else:
                 line_number = 0
                 for line in lines1:
                    avg += float(line.split(" ")[4])
                    line_number += 1
                 avg = float(avg/line_number)
                 avg = format(avg,'.2f')
                print('sdsd')#lineNeedid[0].split('\n'),'nnn',path_need.split("/")[len(path_need.split("/"))-1].split(".")[0])
                total_file = open(self.path, "a",encoding='utf-8')
                total_file.write(" need: "+self.myar[2] +" "+" average: "+str(avg)+' '+" "+" needID: "+self.myar[0].split('\n')[0] +"\n")
                total_file.close()


        print('we came there filter')
        #self.path = path_need
        self.my_need = []
        self.my_avg = []
        need = []
        avg = []
        needId = []
        print('heree1')
        #if os.stat(self.path).st_size == 0:

        print('uuuuuu',self.path)
        total_file = open(self.path, "r",encoding='utf-8')
        print('after print')
        lines = total_file.readlines()
        total_file.close()
        print('line',lines)
        for line in lines:
            print('in for')
            line = re.split(':', line)

            print('lineIS',line)
            need.append(line[1].split()[0])
            avg.append(float(line[2].split()[0]))
            #avg.append(float(line.split(":")[1]))
            print('after avg', line[3], len(line[3]))
            needId.append(line[3].split(' ')[1])
        self.need_avg = self.bubbleSort(needId,avg, need)
        self.array_width = 50

        self.first = QPushButton('show the sort need', self)
        self.first.setStyleSheet("background-color: White")
        self.first.clicked.connect(self.add_scrol)
        self.first.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #self.firstVertical.addWidget(self.first)
        self.first.resize(300, 30)
        self.first.move(150, int(mywidth/3) )
        self.lo = len(self.need_avg[0])


    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def button_click1(self):
        exit()

    def add_scrol(self):
        myscreen = QDesktopWidget().screenGeometry()
        mywidth = myscreen.width() * 45 / 100
        myheight = myscreen.height() * 25 / 100
        self.setMinimumSize(int(mywidth), int(myheight))
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 247))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayoutScroll = QVBoxLayout(self.scrollAreaWidgetContents)
        self.my_need = []
        for i in range(self.lo):
             self.array_width += 40
             self.my_need.append(QPushButton(self.scrollAreaWidgetContents))#str(self.need_avg[1][i])
             #print(str(self.need_avg[2][i]),)
             avgg = format(self.need_avg[1][i],'.2f')

             self.my_need[i].setText('need: '+self.need_avg[0][i]+' '+','+' average: '+str(avgg)+' '+','+'  needID: '+ str(self.need_avg[2][i]))
             self.my_need[i].resize(300, 30)
             self.my_need[i].clicked.connect(self.button_click34)
             self.my_need[i].setCheckable(True)
             self.my_need[i].move(20, self.array_width)

             self.verticalLayoutScroll.addWidget(self.my_need[i])
        self.pb1 = QPushButton('finish', self.scrollAreaWidgetContents)
        self.pb1.clicked.connect(self.button_click1)
        self.pb1.resize(300, 30)
        self.pb1.move(20, self.array_width+100)
        self.verticalLayoutScroll.addWidget(self.pb1)

        self.pb2 = QPushButton('add new information', self.scrollAreaWidgetContents)
        self.pb2.clicked.connect(self.button_click2)
        self.pb2.resize(300, 30)
        self.pb2.move(20, self.array_width + 100)
        self.verticalLayoutScroll.addWidget(self.pb2)

    def button_click2(self):
        print('click on startagain')
        self.hide()
        self.main33 = welcome.Welcome()
        self.main33.show()
        #return final_tansa.welcome.Welcome()
        #self.bar1.show()
    def button_click34(self):
 
        for i in range(len(self.need_avg[0])):
            if self.my_need[i].isChecked() == True:
                self.my_need[i].setChecked(False)
                self.show_need = Show_need(self.need_avg[2][i])
                self.show_need.show()



    def bubbleSort(self,idnumb,alist, al):
   
        list = []
        for passnum in range(len(alist) - 1, 0, -1):
            for i in range(passnum):
                if alist[i] < alist[i + 1]:
                    temp = alist[i]
                    alist[i] = alist[i + 1]
                    alist[i + 1] = temp
                    temp1 = al[i]
                    al[i] = al[i + 1]
                    al[i + 1] = temp1
                    temp2 = idnumb[i]
                    idnumb[i] = idnumb[i+1]
                    idnumb[i+1] = temp2
        list.append(al)
        list.append(alist)
        list.append(idnumb)
        return list
