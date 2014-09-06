import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import setAlarmTimeDialog_ui

class SetAlarmTimeDialog(QDialog, setAlarmTimeDialog_ui.Ui_setAlarmTimeDialog):
   def __init__(self, alarmTime, parent=None):
      super(SetAlarmTimeDialog, self).__init__(parent)
      self.setupUi(self)
      self.timeEdit.setTime(alarmTime)
      self.alarmTime = alarmTime

      self.buttonBox.accepted.connect(self.accept)
      self.buttonBox.rejected.connect(self.reject)

   def accept(self):
      self.alarmTime = self.timeEdit.time()
      QDialog.accept(self)      
