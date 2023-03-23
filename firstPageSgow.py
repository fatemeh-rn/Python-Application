


from PyQt5.QtWidgets import ( QCheckBox,
                              QPushButton, QComboBox,
                             QLineEdit,  QMessageBox,
                             )
from PyQt5.QtWidgets import  QLabel,QHBoxLayout, QVBoxLayout,QSizePolicy
from PyQt5.QtWidgets import  QWidget, QDesktopWidget
from PyQt5 import  QtGui, QtCore
import os
from distutils.util import strtobool

class FirstPageShow(QWidget):
    def __init__(self, path, parent=None):

        super(FirstPageShow, self).__init__(parent)
        self.setFont(QtGui.QFont('Arial', 12))
        self.checks()

        print('here in FirstPageSgow')
       # print('windowwwww manager')

        self.mainLayout = QVBoxLayout()#BoxLayout()
        self.mysize = self.frameGeometry().size()
        self.myscreen = QDesktopWidget().screenGeometry()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))

        self.path = path
        self.mywidth = self.myscreen.width()*78/100
        self.myheight = self.myscreen.height()*55/100
        print('before open file')
        file = open(self.path,mode='r',encoding='utf-8')
        print('after print file')
        line = file.readlines()
        myFile = []
        for i in range(len(line)):
            myFile.append(line[i])
        #print(myFile,':myfile')
        #print(mywidth, myheight,'sdfsdf',myscreen.width(),myscreen.height())
        self.setMinimumSize(int(self.mywidth),int(self.myheight))
        self.mywidth = 400
        self.myheight = 400
        self.setMinimumSize(int(self.mywidth),int(self.myheight))
        print('inja chetor')
        self.center()
        self.setWindowTitle('Desplay Information Gain ')
       # QWidget.setFont(self, 20)
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Need ID:')
        self.nameLabel.move(int(self.mywidth/57), int(self.myheight/11))#20, 20)
        self.nameLabel.resize(int(self.mywidth/20), int(self.myheight/20))

        self.nameLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.nameLabel)


        self.line = QLineEdit(myFile[0].split('\n')[0], self)
        self.line.setReadOnly(True)
        self.line.move(int(self.mywidth/15), int(self.myheight/13))#80, 20)
        self.line.resize(int(self.mywidth/17), int(self.myheight/15))#100, 32)

        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.line)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Validation owner:')
        self.nameLabel2.move(int(self.mywidth/57), int(self.myheight/4))#20, 60)

        self.nameLabel2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.nameLabel2)

        self.line2 = QLineEdit(myFile[1].split('\n')[0], self)
        self.line2.setReadOnly(True)
        self.line2.move(int(self.mywidth/9), int(self.myheight/4.4))#130, 60)
        self.line2.resize(int(self.mywidth/12), int(self.myheight/15))#100, 32)

        self.line2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.line2)
      #  self.nameLabel2.setFont(QFontDialog.setFont('Arial', 40))

        self.salutation_lbl = QLabel('Type of need:', self)
        self.salutation_lbl.move(int(self.mywidth/4), int(self.myheight/11))#300, 20)  # offset the first control 5px

        self.salutation_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation_lbl)
        # from top and left
        self.salutations = [myFile[3].split('\n')[0]]
        self.salutation = QComboBox(self)
        self.salutation.addItems(self.salutations)
        self.salutation.setMinimumWidth(int(self.myheight/10))
        self.salutation.move(int(self.mywidth/3.1), int(self.myheight/11))

        self.salutation.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation)

        self.salutation1_lbl = QLabel('Classification Of Age Related To Need:', self)
        self.salutation1_lbl.move(int(self.mywidth/2), int(self.myheight/11))  # offset the first control 5px

        self.salutation_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation1_lbl)
        # from top and left
        # from top and left
        self.salutations1 = [myFile[4].split('\n')[0]]
        self.salutation1 = QComboBox(self)
        self.salutation1.addItems(self.salutations1)
        self.salutation1.setMinimumWidth(int(self.myheight/10))
        self.salutation1.move(int(self.mywidth/1.5), int(self.myheight/11))

        self.salutation1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation1)

        self.salutation2_lbl = QLabel('Novelty of Need Area:', self)
        self.salutation2_lbl.move(int(self.mywidth/1.2), int(self.myheight/11))  # offset the first control 5px

        self.salutation2_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation2_lbl)
        # from top and left
        self.salutations2 = [myFile[5].split('\n')[0]]
        self.salutation2 = QComboBox(self)
        self.salutation2.addItems(self.salutations2)
        self.salutation2.setMinimumWidth(int(self.myheight/10))
        self.salutation2.move(int(self.mywidth/1.07), int(self.myheight/11))#1330, 20)

        self.salutation2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation2)

        self.salutation3_lbl = QLabel('Area of Need:', self)
        self.salutation3_lbl.move(int(self.mywidth/4), int(self.myheight/4))#300, 60)  # offset the first control 5px
        self.salutation3_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation3_lbl)

        # from top and left

        bbo = False
        self.salutation3 = QCheckBox('physican',self)
        self.salutation3.setChecked(strtobool(myFile[6].split('\n')[0]))
        self.salutation3.move(int(self.mywidth/3.1), int(self.myheight/4))#400,60)
        self.salutation3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation3)
        self.salutation4 = QCheckBox('patient',self)
        self.salutation4.setChecked(strtobool(myFile[7].split('\n')[0]))
        self.salutation4.move(int(self.mywidth/2.5), int(self.myheight/4))#500, 60)
        self.salutation4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation4)
        self.salutation5 = QCheckBox('facilities',self)
        self.salutation5.setChecked(strtobool(myFile[8].split('\n')[0]))
        self.salutation5.move(int(self.mywidth/2.098), int(self.myheight/4))#600, 60)
        self.salutation5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation5)
        self.salutation6 = QCheckBox('equipment',self)
        self.salutation6.setChecked(strtobool(myFile[9].split('\n')[0]))
        self.salutation6.move(int(self.mywidth/1.8), int(self.myheight/4))#700, 60)
        self.salutation6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation6)
        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('need:')
        self.nameLabel4.move(int(self.mywidth/57), int(self.myheight/2.5))#20, 100)
        self.nameLabel4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.nameLabel4)
        self.line4 = QLineEdit(myFile[2].split('\n')[0], self)
        self.line4.setReadOnly(True)
        self.line4.move(int(self.mywidth/10.33), int(self.myheight/2.6))#130, 100)
        self.line4.resize(int(self.mywidth/2.8), int(self.myheight/13))#500, 50)
        self.line4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.line4)

        self.nameLine = QLineEdit('Comment:',self)
        self.nameLine.setReadOnly(True)
        self.nameLine.move(int(self.mywidth/1.22), int(self.myheight/1.5))#1100,400)
        self.nameLine.resize(int(self.mywidth/3.36), int(self.myheight/3.6))#int(self.mywidth/3.36), int(self.myheight/3.6))#400, 150)
        self.nameLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.nameLine)

       # self.name = favourite_name.split(',')
       # print(self.name,'name',self.name[0])
        print('ddddddd')
        self.nameLabel3 = QLabel('personal favourite:', self)
        self.nameLabel3.move(int(self.mywidth/57), int(self.myheight/2.07))#20, 160)  # offset the first control 5px
        self.nameLabel3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.nameLabel3)
       # self.myarray = []
       # self.aarray_len = self.name.__len__()
        #self.array_width = int(self.myheight/16)
        print('ghable chap')
        '''
        for i in range(self.aarray_len):
            self.myarray.append(QCheckBox(self.name[i],self))
            #self.myarray[i] = QCheckBox(self.name[i],self)
            self.myarray[i].setChecked(False)
            self.array_width += int(self.myheight/3)
            self.myarray[i].move(self.array_width,int(self.myheight/2.07))
            self.myarray[i].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.mainLayout.addWidget(self.myarray[i])
        '''
        print('inja dg chap kon')
        self.myarrayfirst = []
        count = len(myFile)
        # print(count,type(count))
        self.array_width = 50
        x = 0
        for i in range(10, count):
            # print(myFile[i].split('\n')[0].split(' ')[0], 'whatt',strtobool(myFile[i].split('\n')[0].split(' ')[1]))
            self.myarrayfirst.append(QCheckBox(myFile[i].split('\n')[0].split(' ')[0], self))
     
            self.myarrayfirst[x].setChecked(strtobool(myFile[i].split('\n')[0].split(' ')[1]))
            self.array_width += 100
            self.myarrayfirst[x].move(self.array_width, 160)
            self.myarrayfirst[x].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.mainLayout.addWidget(self.myarrayfirst[x])
            x += 1
        self.pb = QPushButton('ok',self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(self.button_click)
        self.pb.resize(int(self.mywidth/13.44), int(self.myheight/13.5))#100, 40)
        self.pb.move(int(self.mywidth/27), int(self.myheight/1.35))#50, 400)
        self.pb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.pb)
        
        self.setLayout(self.mainLayout)

    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)


    def center(self):
        print('center firstpageshow')
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


    def button_click(self):
        print("asan moad firsipageshow")
        self.hide()
