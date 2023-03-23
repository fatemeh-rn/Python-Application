
from PyQt5.QtWidgets import (QPushButton, QLineEdit, QMessageBox)
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QGridLayout, QSizePolicy,  QHBoxLayout, QVBoxLayout
from manager import Window
from PyQt5 import  QtGui, QtCore
import os

class Welcome(QWidget):
    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent)
        print('in new_welcom')
        self.checks()
        self.setFont(QtGui.QFont('Arial', 12))

        self.layoutGrid = QGridLayout()
        self.setLayout(self.layoutGrid)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'tansa.png'))

        self.setWindowTitle('Wellcome !')

        # print('we came there wellcome')
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('please enter your partner: ')
        self.nameLabel.move(140, 100)
        self.layoutGrid.addWidget(self.nameLabel)

        self.line = QLineEdit(self)
        # self.line.move(mywidth*)#300, 100)
        # self.line.resize(300, 32)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layoutGrid.addWidget(self.line)

        self.pb = QPushButton('ok', self)
        self.pb.setStyleSheet("background-color: White")
        self.pb.clicked.connect(self.button_click1)
        self.pb.resize(100, 40)
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.pb)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)
        # self.pb.move(280, 200)
        # self.line.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.layoutGrid.addWidget(self.pb)


        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText('NOTE: please insert names in english and seprate them by comma ')
        # self.nameLabel1.move(680, 90)
        # self.nameLabel1.resize(250, 50)
        self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layoutGrid.addWidget(self.nameLabel1)

    def checks(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)  # darkCyan
        self.setPalette(p)

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        # print(self.size(),'size')

    def button_click1(self):
        # print('i m here in ok')
        if self.line.text() == '':
            msg1 = QMessageBox(self)
            self.messageBox = msg1
            msg1.setText('please full the blank!')
            msg1.setWindowTitle('Alert')
            # msg1.resize(600, 400)
            self.line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.layoutGrid.addWidget(self.messageBox)
            # print('came oweeeer')
            msg1.show()

        else:
            numb = self.line.text()
            self.hide()
            self.main11 = Window(numb, "data")
            self.main11.show()



