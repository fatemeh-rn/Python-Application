from sys import exit
from PyQt5.QtWidgets import QApplication

from welcome import Welcome



import sys, os

def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
  
    app = QApplication(sys.argv)
    main = Welcome()
    main.show()
    sys.exit(app.exec_())
