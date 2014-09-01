import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import setAlarmTimeDialog_ui

class SetAlarmTimeDialog(QDialog, setAlarmTimeDialog_ui.Ui_setAlarmTimeDialog):
   def __init__(self, parent=None):
      super(SetAlarmTimeDialog, self).__init__(parent)
      self.setupUi(self)
