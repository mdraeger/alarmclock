import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from translate import _translate

import chooseAlarmDialog_ui

class ChooseAlarmDialog(QDialog, chooseAlarmDialog_ui.Ui_chooseAlarmDialog):
   def __init__(self, parent=None):
      super(ChooseAlarmDialog, self).__init__(parent)
      self.setupUi(self)
      self.openFileDialogButton.clicked.connect(self.chooseFile)
      self.buttonBox.accepted.connect(self.accept)
      self.buttonBox.rejected.connect(self.reject)
      self.alarmSongPath = ""

   def chooseFile(self):
      dialog = QFileDialog(self)
      dialog.resize(300,200)  
      fileName = dialog.getOpenFileName(self, caption=_translate("alarmclock", "Wecklied aussuchen",     None), directory=".",filter=_translate("alarmclock", "Audio files *.mp3 *.ogg *.wav", None))
      self.pathToFileEdit.setText(fileName)

   def accept(self):
      self.alarmSongPath = self.pathToFileEdit.text()
      QDialog.accept(self)

