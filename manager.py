


from PyQt5.QtWidgets import ( QCheckBox,
                              QPushButton, QComboBox,
                             QLineEdit,  QMessageBox,
                             )
from PyQt5.QtWidgets import  QLabel,QHBoxLayout, QVBoxLayout,QSizePolicy
from PyQt5.QtWidgets import  QWidget, QDesktopWidget

from priamary_filtering import PrimaryFiltering
from PyQt5 import  QtGui, QtCore
import os

class Window(QWidget):
    def __init__(self,favourite_name, path, parent=None):

        super(Window, self).__init__(parent)
        self.checks()
        self.setFont(QtGui.QFont('Arial', 12))

       # print('windowwwww manager')

        self.mainLayout = QVBoxLayout()#BoxLayout()
        self.mysize = self.frameGeometry().size()
        self.myscreen = QDesktopWidget().screenGeometry()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))


        self.path = path
        self.mywidth = 400
        self.myheight = 400
        self.setMinimumSize(int(self.mywidth),int(self.myheight))
        self.center()
        self.setWindowTitle('information gain')
       # QWidget.setFont(self, 20)
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Need ID:')
        self.nameLabel.move(int(self.mywidth/57), int(self.myheight/20))#20, 20)
        self.nameLabel.resize(int(self.mywidth/20), int(self.myheight/20))

        self.nameLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.nameLabel)



        self.line = QLineEdit(self)
        self.line.move(int(self.mywidth/15), int(self.myheight/13))#80, 20)
        self.line.resize(int(self.mywidth/17), int(self.myheight/15))#100, 32)

        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.line)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Validation owner:')
        self.nameLabel2.move(int(self.mywidth/57), int(self.myheight/4))#20, 60)

        self.nameLabel2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.nameLabel2)
        self.line2 = QLineEdit(self)
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
        self.salutations = ['select','Incremental',
                            'Blue Sky',
                            'Mixed']
        self.salutation = QComboBox(self)
        self.salutation.addItems(self.salutations)
        self.salutation.setMinimumWidth(int(self.myheight/10))
        self.salutation.move(int(self.mywidth/3.1), int(self.myheight/11))

        self.salutation.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation)

        self.salutation1_lbl = QLabel('Classification of Age Related to Need:', self)
        self.salutation1_lbl.move(int(self.mywidth/2), int(self.myheight/11))  # offset the first control 5px

        self.salutation_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation1_lbl)
        # from top and left
        self.salutations1 = ['select',
                            'Baby',
                            'Child',
                            'Young',
                            'Middle Old',
                            'Old',
                            'All Of Ages',
                            'None']
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
        self.salutations2 = ['select',
                             'Yes',
                             'No']
        self.salutation2 = QComboBox(self)
        self.salutation2.addItems(self.salutations2)
        self.salutation2.setMinimumWidth(int(self.myheight/10))
        self.salutation2.move(int(self.mywidth/1.07), int(self.myheight/11))#1330, 20)

        self.salutation2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation2)

        self.salutation3_lbl = QLabel('Area Of Need:', self)
        self.salutation3_lbl.move(int(self.mywidth/4), int(self.myheight/4))#300, 60)  # offset the first control 5px
        self.salutation3_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation3_lbl)

        # from top and left
        self.salutations3 = ['select',
                             'patient',
                             'eqipment',
                             'facilities',
                             'physican']
        bbo = False
        self.salutation3 = QCheckBox('physican',self)
        self.salutation3.setChecked(bbo)
        self.salutation3.move(int(self.mywidth/3.1), int(self.myheight/4))#400,60)
        self.salutation3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation3)
        self.salutation4 = QCheckBox('patient',self)
        self.salutation4.setChecked(bbo)
        self.salutation4.move(int(self.mywidth/2.5), int(self.myheight/4))#500, 60)
        self.salutation4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation4)
        self.salutation5 = QCheckBox('facilities',self)
        self.salutation5.setChecked(bbo)
        self.salutation5.move(int(self.mywidth/2.098), int(self.myheight/4))#600, 60)
        self.salutation5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation5)
        self.salutation6 = QCheckBox('equipment',self)
        self.salutation6.setChecked(bbo)
        self.salutation6.move(int(self.mywidth/1.8), int(self.myheight/4))#700, 60)
        self.salutation6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.salutation6)
        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('need:')
        self.nameLabel4.move(int(self.mywidth/57), int(self.myheight/2.5))#20, 100)
        self.nameLabel4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.nameLabel4)
        self.line4 = QLineEdit(self)
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

        self.name = favourite_name.split(',')
       # print(self.name,'name',self.name[0])

        self.nameLabel3 = QLabel('personal favourite:', self)
        self.nameLabel3.move(int(self.mywidth/57), int(self.myheight/2.07))#20, 160)  # offset the first control 5px
        self.nameLabel3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.nameLabel3)
        self.myarray = []
        self.aarray_len = self.name.__len__()
        self.array_width = int(self.myheight/16)
        for i in range(self.aarray_len):
            self.myarray.append(QCheckBox(self.name[i],self))
            #self.myarray[i] = QCheckBox(self.name[i],self)
            self.myarray[i].setChecked(False)
            self.array_width += int(self.myheight/3)
            self.myarray[i].move(self.array_width,int(self.myheight/2.07))
            self.myarray[i].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.mainLayout.addWidget(self.myarray[i])
        self.pb = QPushButton('ok',self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(self.button_click)
        self.pb.resize(int(self.mywidth/13.44), int(self.myheight/13.5))#100, 40)
        self.pb.move(int(self.mywidth/27), int(self.myheight/1.35))#50, 400)
        self.pb.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.pb)
        #print('finallllllllll')
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



    def button_click(self):
        # shost is a QString object



        if self.line.text() == '' or self.line2.text() == '' or self.line4.text() == ''\
                or self.salutation.currentText() == 'select' or self.salutation1.currentText() == 'select' or self.salutation2.currentText() == 'select'  :
            msg1 = QMessageBox(self)
            self.messageBox = msg1
            msg1.setText('please full the blank!')
            msg1.setWindowTitle('Alert')
            msg1.resize(600, 400)
           # print('came oweeeer')
            msg1.show()
        elif self.salutation3.isChecked() == False and self.salutation4.isChecked() == False\
               and self.salutation5.isChecked()== False and self.salutation6.isChecked() == False:
             msg1 = QMessageBox(self)
             self.messageBox = msg1
             msg1.setText('please full at least one area!')
             msg1.setWindowTitle('Alert')
             msg1.resize(600, 400)
           #  print('came oweeeer')
             msg1.show()
        else:
         self.shost = self.line.text()
         self.shost2 = self.line2.text()
         self.shost4 = self.line4.text()
         self.myoption = self.salutation.currentText()
         self.myoption1 = self.salutation1.currentText()
         self.myoption2 = self.salutation2.currentText()
         self.phycheck = self.salutation3.isChecked()
         self.pcheck = self.salutation4.isChecked()
         self.fcheck = self.salutation5.isChecked()
         self.echeck = self.salutation6.isChecked()
         self.array_check_name = []
         counter = 0
         if self.phycheck:
            counter += 1
         if self.pcheck:
            counter += 1
         if self.fcheck:
            counter += 1
         if self.echeck:
            counter += 1

         self.myar = []
         self.myar.append(self.shost)
         self.myar.append(self.shost2)
         self.myar.append(self.shost4)
         self.myar.append(self.myoption)
         self.myar.append(self.myoption1)
         self.myar.append(self.myoption2)
         self.myar.append(self.phycheck)
         self.myar.append(self.pcheck)
         self.myar.append(self.fcheck)
         self.myar.append(self.echeck)
        # print(type(self.name[0]),'fff:',type(self.myarray[0].isChecked()))
         for i in range(self.aarray_len):
            strr = self.name[i] +' '+str (self.myarray[i].isChecked())
            self.myar.append(strr)
         self.mypatth = self.path +'/' +'page1_'+self.shost+ '.txt'

         for i in range(self.aarray_len):
            self.array_check_name.append(self.myarray[i].isChecked())#maslan injuri mishavad:item_check_o = false
        # print(self.array_check_name[0],'whatttt??')

         self.hide()
         number_true = 0
         print('inGeneral:counterIs:',counter)
         self.main3 = PrimaryFiltering(self.phycheck,self.pcheck,self.fcheck,self.echeck,self.path +'/' +'pagetotal_'+self.shost+ '.txt', counter,self.myar)
         self.main3.show()

