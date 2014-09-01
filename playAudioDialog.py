import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from translate import _translate

import playAudioDialog_ui

import player

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
      self.sleepTimer = QTimer(self)
      self.sleepTimer.setSingleShot(True)

   def chooseFileAndSetSleepMode(self):
      fileName = QFileDialog.getOpenFileName(self, caption="Wecklied aussuchen", directory=".",filter="Audio files *.mp3 *.ogg *.wav")
      self.lineEdit.setText(fileName)

   def toggleSleepTimeEdit(self):
      self.sleepTimeEdit.setEnabled(self.sleepModeCheckBox.isChecked())

   def accept(self):
      self.filePath = self.lineEdit.text()
      self.sleep = self.sleepModeCheckBox.isChecked()
      if self.sleep:
         sleepTime = self.sleepTimeEdit.time()
         self.sleepTimer.start((sleepTime.hour()*60+sleepTime.minute())*60*1000)
      QDialog.accept(self)
