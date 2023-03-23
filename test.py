# # # # # import sys
# # # # # from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
# # # # # from PyQt5.QtGui import QIcon
# # # # # from PyQt5.QtCore import pyqtSlot
# # # # #
# # # # #
# # # # # class App(QDialog):
# # # # #
# # # # #     def __init__(self):
# # # # #         super().__init__()
# # # # #         self.title = 'PyQt5 layout - pythonspot.com'
# # # # #         self.left = 10
# # # # #         self.top = 10
# # # # #         self.width = 320
# # # # #         self.height = 100
# # # # #         self.initUI()
# # # # #
# # # # #     def initUI(self):
# # # # #         self.setWindowTitle(self.title)
# # # # #         self.setGeometry(self.left, self.top, self.width, self.height)
# # # # #
# # # # #         self.createHorizontalLayout()
# # # # #
# # # # #         windowLayout = QVBoxLayout()
# # # # #         windowLayout.addWidget(self.horizontalGroupBox)
# # # # #         self.setLayout(windowLayout)
# # # # #
# # # # #         self.show()
# # # # #
# # # # #     def createHorizontalLayout(self):
# # # # #         self.horizontalGroupBox = QGroupBox("What is your favorite color?")
# # # # #         layout = QHBoxLayout()
# # # # #
# # # # #         buttonBlue = QPushButton('Blue', self)
# # # # #         buttonBlue.clicked.connect(self.on_click)
# # # # #         layout.addWidget(buttonBlue)
# # # # #
# # # # #         buttonRed = QPushButton('Red', self)
# # # # #         buttonRed.clicked.connect(self.on_click)
# # # # #         layout.addWidget(buttonRed)
# # # # #
# # # # #         buttonGreen = QPushButton('Green', self)
# # # # #         buttonGreen.clicked.connect(self.on_click)
# # # # #         layout.addWidget(buttonGreen)
# # # # #
# # # # #         self.horizontalGroupBox.setLayout(layout)
# # # # #
# # # # #     @pyqtSlot()
# # # # #     def on_click(self):
# # # # #         print('PyQt5 button click')
# # # # #
# # # # #
# # # # # if __name__ == '__main__':
# # # # #     app = QApplication(sys.argv)
# # # # #     ex = App()
# # # # #     sys.exit(app.exec_())
# # # # #
# # # #
# # # #
# # # # import sys
# # # #
# # # # import self as self
# # # # from PyQt5.QtCore import *
# # # # from PyQt5.QtGui import *
# # # # from PyQt5.QtWidgets import QMainWindow, QAction, QMdiArea, QApplication, QMdiSubWindow, QTextEdit
# # # #
# # # #
# # # # class MainWindow(QMainWindow):
# # # #     count = 0
# # # #
# # # #     def __init__(self, parent=None):
# # # #         super(MainWindow, self).__init__(parent)
# # # #         self.mdi = QMdiArea()
# # # #         self.setCentralWidget(self.mdi)
# # # #         bar = self.menuBar()
# # # #
# # # #         file = bar.addMenu("File")
# # # #         file.addAction("New")
# # # #         file.addAction("cascade")
# # # #         file.addAction("Tiled")
# # # #         file.triggered[QAction].connect(self.windowaction)
# # # #         self.setWindowTitle("MDI demo")
# # # #
# # # #     def windowaction(self, q):
# # # #      print("triggered")
# # # #
# # # #      if q.text() == "New":
# # # #         MainWindow.count = MainWindow.count + 1
# # # #         sub = QMdiSubWindow()
# # # #         sub.setWidget(QTextEdit())
# # # #         sub.setWindowTitle("subwindow" + str(MainWindow.count))
# # # #         self.mdi.addSubWindow(sub)
# # # #         sub.show()
# # # #
# # # #      if q.text() == "cascade":
# # # #         self.mdi.cascadeSubWindows()
# # # #
# # # #      if q.text() == "Tiled":
# # # #         self.mdi.tileSubWindows()
# # # #
# # # #     def main(self):
# # # #         app = QApplication(sys.argv)
# # # #         ex = MainWindow()
# # # #         ex.show()
# # # #         sys.exit(app.exec_())
# # # #
# # # #     if __name__ == '__main__':
# # # #         main(self)
# # #
# # # import sys
# # # from PyQt5.QtCore import *
# # # from PyQt5.QtGui import *
# # # from PyQt5.QtWidgets import QTabWidget, QWidget, QFormLayout, QLineEdit, QHBoxLayout, QRadioButton, QLabel, QCheckBox, \
# # #     QApplication
# # #
# # #
# # # class tabdemo(QTabWidget):
# # #     def __init__(self, parent=None):
# # #         super(tabdemo, self).__init__(parent)
# # #         self.tab1 = QWidget()
# # #         self.tab2 = QWidget()
# # #         self.tab3 = QWidget()
# # #
# # #         self.addTab(self.tab1, "Tab 1")
# # #         self.addTab(self.tab2, "Tab 2")
# # #         self.addTab(self.tab3, "Tab 3")
# # #         self.tab1UI()
# # #         self.tab2UI()
# # #         self.tab3UI()
# # #         self.setWindowTitle("tab demo")
# # #
# # #     def tab1UI(self):
# # #         layout = QFormLayout()
# # #         layout.addRow("Name", QLineEdit())
# # #         layout.addRow("Address", QLineEdit())
# # #         self.setTabText(0, "Contact Details")
# # #         self.tab1.setLayout(layout)
# # #
# # #     def tab2UI(self):
# # #         layout = QFormLayout()
# # #         sex = QHBoxLayout()
# # #         sex.addWidget(QRadioButton("Male"))
# # #         sex.addWidget(QRadioButton("Female"))
# # #         layout.addRow(QLabel("Sex"), sex)
# # #         layout.addRow("Date of Birth", QLineEdit())
# # #         self.setTabText(1, "Personal Details")
# # #         self.tab2.setLayout(layout)
# # #
# # #     def tab3UI(self):
# # #         layout = QHBoxLayout()
# # #         layout.addWidget(QLabel("subjects"))
# # #         layout.addWidget(QCheckBox("Physics"))
# # #         layout.addWidget(QCheckBox("Maths"))
# # #         self.setTabText(2, "Education Details")
# # #         self.tab3.setLayout(layout)
# # #
# # #
# # # def main():
# # #     app = QApplication(sys.argv)
# # #     ex = tabdemo()
# # #     ex.show()
# # #     sys.exit(app.exec_())
# # #
# # #
# # # if __name__ == '__main__':
# # #     main()
# #
# #
# #
# # import sys
# # from PyQt5.QtCore import *
# # from PyQt5.QtGui import QIntValidator, QFont, QDoubleValidator, QStandardItemModel, QStandardItem, QPalette, QColor
# # from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
# #                              QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider, QSizePolicy, QComboBox,
# #                              QLineEdit, QFormLayout, QInputDialog, QLabel, QListView, QHBoxLayout, QMessageBox,
# #                              QDesktopWidget, QScrollArea, QScrollBar)
# # from PyQt5.QtWidgets import QMainWindow, QLabel
# # from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget
# #
# # from show_pages2.show_pages.Show_need import Show_need
# #
# #
# # class End(QWidget):
# #     def __init__(self, path_need, parent=None):
# #         super(End, self).__init__(parent)
# #         self.path = "C:/Users/win_10/Desktop/python.proj/show_pages2/show_pages/data/total.txt"
# #         self.center()
# #         self.setWindowTitle('Show Scores')
# #         print('here in end')
# #         file = open(path_need, "r")
# #         lines1 = file.readlines()
# #         file.close()
# #         #print(lines1,'liness1',self.path,'my_path',path_need)
# #         avg = 0.0
# #         line_number = 0
# #         for line in lines1:
# #             avg += float(line.split(" ")[4])
# #             line_number += 1
# #         avg = float(avg/line_number)
# #         thispath = path_need.split('.txt')[0]+'.page1'+'.txt'
# #         file_needid = open(thispath,'r')
# #         lineNeedid = file_needid.readlines()
# #         file_needid.close()
# #         print(lineNeedid[0].split('\n'),'nnn')
# #         total_file = open(self.path, "a")
# #         total_file.write(path_need.split("/")[len(path_need.split("/"))-1].split(".")[0] + " " + str(avg)+' '+lineNeedid[0].split('\n')[0] + "\n")
# #         total_file.close()
# #         self.center()
# #         self.setWindowTitle('Show Scores')
# #         #print('we came there filter')
# #         #self.path = path_need
# #         self.my_need = []
# #         self.my_avg = []
# #         need = []
# #         avg = []
# #         print('heree1')
# #         total_file = open(self.path, "r")
# #         lines = total_file.readlines()
# #         total_file.close()
# #         #print('line',lines)
# #         for line in lines:#age farsi bashe mshe[1] age englisi bashe mshe [0]chon az chap b rast minevise
# #             need.append(line.split(" ")[0])
# #             # print('kk: ',line)
# #             # print('lllll: ',line.split(" ")[1])
# #             avg.append(float(line.split(" ")[1]))
# #         #print(avg,' :avg: ',need)
# #         self.need_avg = self.bubbleSort(avg, need)
# #         self.array_width = 50
# #         #print(self.need_avg[0],'ajb')
# #         # self.s1 = QScrollBar()
# #         # self.s1.setMaximum(255)
# #         # self.s1.sliderMoved.connect(self.sliderval)
# #         #print(len(self.need_avg[0]),'length')
# #         #print('here22')
# #         self.first = QPushButton('score                                          need', self)
# #         #self.first.clicked.connect(self.button_click1)
# #         self.first.resize(300, 30)
# #         self.first.move(20, 30)
# #         self.lo = len(self.need_avg[0])
# #         print(self.need_avg[0],'say need avg',self.need_avg[1])
# #         for i in range(self.lo):
# #
# #              self.array_width += 30
# #              self.my_need.append(QPushButton(self.need_avg[0][i], self))
# #              self.my_need[i].resize(300, 30)
# #              self.my_need[i].clicked.connect(self.button_click)
# #              self.my_need[i].setCheckable(True)
# #              self.my_need[i].move(20, self.array_width)
# #
# #              self.my_avg.append(QLabel(str(self.need_avg[1][i]), self))
# #              self.my_avg[i].setText(str(self.need_avg[1][i]))
# #              self.my_avg[i].move(50, self.array_width)
# #
# #         self.pb = QPushButton('ok', self)
# #         self.pb.clicked.connect(self.button_click1)
# #         self.pb.resize(50, 50)
# #         self.pb.move(400, 200)
# #
# #     def sliderval(self):
# #         print(self.s1.value())
# #         palette = QPalette()
# #         self.l1.setPalette(palette)
# #
# #     def center(self):
# #         frameGm = self.frameGeometry()
# #         centerPoint = QDesktopWidget().availableGeometry().center()
# #         frameGm.moveCenter(centerPoint)
# #         self.move(frameGm.topLeft())
# #     def button_click1(self):
# #         exit()
# #     def button_click(self):
# #
# #         #path = 'C:/Users/win_10/Desktop/python.proj/show_pages2/show_pages/data/' + self.need_avg[0][0] + '.txt'
# #        # print(self.need_avg[0][2],'mmmmmmmm')
# #         for i in range(len(self.need_avg[0])):
# #             if self.my_need[i].isChecked() == True:
# #                 #path = 'C:/Users/win_10/Desktop/python.proj/show_pages2/show_pages/data/' + self.need_avg[0][i] + '.txt'
# #                 #print(self.need_avg[0][i],'my_path')
# #                 self.show_need = Show_need(self.need_avg[0][i])
# #                 self.show_need.show()
# #
# #
# #     def bubbleSort(self,alist, al):
# #         print("alist",alist)
# #         print("al",al)
# #         print('here in bubble')
# #         list = []
# #         for passnum in range(len(alist) - 1, 0, -1):
# #             for i in range(passnum):
# #                 if alist[i] < alist[i + 1]:
# #                     temp = alist[i]
# #                     alist[i] = alist[i + 1]
# #                     alist[i + 1] = temp
# #                     temp1 = al[i]
# #                     al[i] = al[i + 1]
# #                     al[i + 1] = temp1
# #         list.append(al)
# #         list.append(alist)
# #         return list
# #
# #
# #     # noinspection PyTypeChecker
# #     # def button_click2(self,op1, op2, op3, op4):
# #     #     pass
# #
# #
# #
# #     # noinspection PyTypeChecker
# #     # def button_click2(self,op1, op2, op3, op4):
# #     #     pass
# from PyQt5.QtWidgets import QScrollBar
#
#
# def _update_output(self):
#     scrollbar = self.outputEdit.verticalScrollBar()
#     assert isinstance(scrollbar, QScrollBar)
#     # Preserve scroll while updating content
#     current_scroll = scrollbar.value()
#     scrolling = scrollbar.isSliderDown()
#
#     with self._flash_output_mutex:
#         self.outputEdit.setPlainText(self._flash_output.decode('utf-8', errors="ignore"))
#
#     if not scrolling:
#         scrollbar.setValue(scrollbar.maximum())
#     else:
#         scrollbar.setValue(current_scroll)


from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QScrollArea, QApplication, QDialog, QTextEdit


class myDialog(QDialog):
    _buttons = 0

    def __init__(self, parent=None):
        super(myDialog, self).__init__(parent)

        self.pushButton = QPushButton(self)
        self.pushButton.setText(QApplication.translate("self", "Add Button!", None))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.scrollArea =QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.move(500,500)
        self.scrollAreaWidgetContents.resize(1000,500)
        #self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 10, 90))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalLayoutScroll =QVBoxLayout(self.scrollAreaWidgetContents)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
      self._buttons  += 1
      pushButton = []
      for i in range(10):
        pustButtonName = 'c'

        pushButton.append(QPushButton(self.scrollAreaWidgetContents))
        pushButton[i].se#.setText(pustButtonName)

        self.verticalLayoutScroll.addWidget(pushButton[i])


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('myDialog')

    main = myDialog()
    main.show()

    sys.exit(app.exec_())

    #add icon:
    '''
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(myfirstgui.sizePolicy().hasHeightForWidth())
    myfirstgui.setSizePolicy(sizePolicy)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("logo_fZG_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    myfirstgui.setWindowIcon(icon)
    '''