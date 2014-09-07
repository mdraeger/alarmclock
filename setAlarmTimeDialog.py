##    alarmclock (resembles a an alarm clock for raspberry pi with a 
##    2.8" LCD touch display 
##    Copyright (C) 2014  Marco Draeger
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
