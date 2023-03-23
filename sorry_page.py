
from PyQt5.QtWidgets import ( QPushButton, )
from PyQt5.QtWidgets import  QWidget

import time
from PyQt5 import QtCore, QtGui
import os

class Sorry_page(QWidget):
    def __init__(self,noscoractive, path,first_aray, parent=None):
        super(Sorry_page, self).__init__(parent)
        #self.center()
        self.checks()
        self.setFont(QtGui.QFont('Arial', 12))

        self.noscoreactive = noscoractive
        self.setWindowTitle('Sorry')
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))
        print('sorry page')
        
        self.pb = QPushButton('ok', self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(self.button_click)
        self.pb.resize(50, 50)
        self.pb.move(340, 200)

        #self.show_message()

    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)

    def button_click(self):
        time.sleep(2)
        exit(3)
      
