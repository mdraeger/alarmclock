import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from translate import _translate

import playAudioDialog_ui

class PlayAudioDialog(QDialog, playAudioDialog_ui.Ui_playAudioDialog):
   def __init__(self, parent=None):
      super(PlayAudioDialog, self).__init__(parent)
      self.setupUi(self)

      self.toolButton.clicked.connect(self.chooseFileAndSetSleepMode)
      self.sleepModeCheckBox.clicked.connect(self.toggleSleepTimeEdit)
      self.buttonBox.accepted.connect(self.accept)
      self.buttonBox.rejected.connect(self.reject)

      self.filePath = ""
      self.sleep = False
      self.sleepTime = self.sleepTimeEdit.time()

   def chooseFileAndSetSleepMode(self):
      fileName = QFileDialog.getOpenFileName(self, caption=_translate("playAudioDialog", "Wecklied aussuchen", None), directory=".",filter=_translate("playAudioDialog", "Audio files *.mp3 *.ogg *.wav", None))
      self.lineEdit.setText(fileName)

   def toggleSleepTimeEdit(self):
      self.sleepTimeEdit.setEnabled(self.sleepModeCheckBox.isChecked())

   def accept(self):
      self.filePath = self.lineEdit.text()
      self.sleep = self.sleepModeCheckBox.isChecked()
      if self.sleep:
         self.sleepTime = self.sleepTimeEdit.time()
      QDialog.accept(self)
