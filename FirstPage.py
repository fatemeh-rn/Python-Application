
from PyQt5.QtWidgets import ( QCheckBox, QPushButton, QComboBox,
                             QLineEdit)
from PyQt5.QtWidgets import  QLabel
from PyQt5.QtWidgets import  QWidget, QDesktopWidget
from distutils.util import strtobool
import os
from PyQt5 import  QtGui, QtCore



class FirstPage(QWidget):
    def __init__(self,path, parent=None):
        super(FirstPage, self).__init__(parent)
        self.setFont(QtGui.QFont('Arial', 12))
        self.checks()
        self.mysize = self.frameGeometry().size()
        myscreen = QDesktopWidget().screenGeometry()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))
        
        self.path = path
        mywidth = myscreen.width()*78/100
        myheight = myscreen.height()*55/100
        file = open(self.path,mode='r',encoding='utf-8')
        line = file.readlines()
        myFile = []
        for i in range(len(line)):
            myFile.append(line[i])
        self.setMinimumSize(mywidth,myheight)
        self.setWindowTitle('information gain:show')
  
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Need ID:')
        self.line = QLineEdit(myFile[0].split('\n')[0],self)
        self.line.setReadOnly(True)
        self.line.move(80, 20)
        self.line.resize(100, 32)
        self.nameLabel.move(20, 20)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Validation owner:')
        self.line2 = QLineEdit(myFile[1].split('\n')[0],self)
        self.line2.setReadOnly(True)
        self.line2.move(130, 60)
        self.line2.resize(100, 32)
        self.nameLabel2.move(20, 60)
        #
        self.salutation_lbl = QLabel('type of need:', self)
        self.salutation_lbl.move(300, 20)  # offset the first control 5px
        # from top and left
        self.salutations = [myFile[3].split('\n')[0]]
        self.salutation = QComboBox(self)
        self.salutation.addItems(self.salutations)
        self.salutation.setMinimumWidth(200)
        self.salutation.move(380, 20)

        self.salutation1_lbl = QLabel('classification of age related to need:', self)
        self.salutation1_lbl.move(680, 20)  # offset the first control 5px
        # from top and left
        self.salutations1 = [myFile[4].split('\n')[0]]
        self.salutation1 = QComboBox(self)
        self.salutation1.addItems(self.salutations1)
        self.salutation1.setMinimumWidth(200)
        self.salutation1.move(900, 20)
        #
        self.salutation2_lbl = QLabel('novelty of need area:', self)
        self.salutation2_lbl.move(1200, 20)  # offset the first control 5px
        # from top and left
        self.salutations2 = [myFile[5].split('\n')[0]]
        self.salutation2 = QComboBox(self)
        self.salutation2.addItems(self.salutations2)
        self.salutation2.setMinimumWidth(200)
        self.salutation2.move(1330, 20)

        #print('area of need')
        self.salutation3_lbl = QLabel('area of need:', self)
        self.salutation3_lbl.move(300, 60)  # offset the first control 5px
        # from top and left
        self.salutation3 = QCheckBox('physican',self)
        self.salutation3.setChecked(strtobool(myFile[6].split('\n')[0]))
        self.salutation3.move(400,60)
        self.salutation4 = QCheckBox('patient',self)
        self.salutation4.setChecked(strtobool(myFile[7].split('\n')[0]))
        self.salutation4.move(500, 60)
        self.salutation5 = QCheckBox('facilities',self)
        self.salutation5.setChecked(strtobool(myFile[8].split('\n')[0]))
        self.salutation5.move(600, 60)
        self.salutation6 = QCheckBox('equipment',self)
        self.salutation6.setChecked(strtobool(myFile[9].split('\n')[0]))
        self.salutation6.move(700, 60)

        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('need:')
        self.line4 = QLineEdit(myFile[2].split('\n')[0],self)
        self.line4.setReadOnly(True)
        self.line4.move(130, 100)
        self.line4.resize(500, 50)
        self.nameLabel4.move(20, 100)

        self.nameLine = QLineEdit('comment sdfs sdfs dfsf sdfsdf sdfsdf    ',self)
        self.nameLine.setReadOnly(True)
        self.nameLine.move(1100,400)
        self.nameLine.resize(400, 150)

        self.nameLabel3 = QLabel('personal favourte:', self)
        self.nameLabel3.move(20, 160)  # offset the first control 5px
        self.myarrayfirst = []
        count = len(myFile)
       # print(count,type(count))
        self.array_width = 50
        x = 0
        for i in range(10,count):
            #print(myFile[i].split('\n')[0].split(' ')[0], 'whatt',strtobool(myFile[i].split('\n')[0].split(' ')[1]))
            self.myarrayfirst.append(QCheckBox(myFile[i].split('\n')[0].split(' ')[0],self))
            
            self.myarrayfirst[x].setChecked(strtobool(myFile[i].split('\n')[0].split(' ')[1]))
            self.array_width += 100
            self.myarrayfirst[x].move(self.array_width,160)
            # if x== 0:self.myarrayfirst[0].move(self.array_width,160)
            # elif x == 1 :self.myarrayfirst[1].move(self.array_width,160)
            x+= 1

        self.pb = QPushButton('ok',self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(self.button_click)
        self.pb.resize(100, 40)
        self.pb.move(50, 400)

    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)

    def button_click(self):
       self.hide()