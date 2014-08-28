import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import alarmclock_ui
import clockWidget

class MainWindow(QMainWindow, alarmclock_ui.Ui_mainWindow):
   def __init__(self, parent=None):
      super(MainWindow, self).__init__(parent)
      self.setupUi(self)
      self.clockWidget = clockWidget.PyAnalogClock(self.clockFrame)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = MainWindow()
   main.show()
   app.exec_()
