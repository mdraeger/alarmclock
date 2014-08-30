import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import alarmclock_ui
import chooseAlarmDialog_ui
import playAudioDialog_ui
import setAlarmTimeDialog_ui
import clockWidget

class MainWindow(QMainWindow, alarmclock_ui.Ui_mainWindow):
   def __init__(self, parent=None):
      super(MainWindow, self).__init__(parent)
      self.setupUi(self)
      self.clockWidget = clockWidget.PyAnalogClock(self.clockFrame)

      self.chooseAlarmSoundButton.clicked.connect(self.chooseAlarm)
      self.listenNowButton.clicked.connect(self.playAudio)
      self.changeAlarmTimeButton.clicked.connect(self.setAlarmTime)

      self.alarmTime = QTime()
      self.alarmSongPath = ""
      self.sleepTime = QTimer()

   def chooseAlarm(self):
      dialog = ChooseAlarmDialog(self)
      if dialog.exec_():
         self.alarmSongPath = dialog.alarmSongPath

   def playAudio(self):
      dialog = PlayAudioDialog(self)
      dialog.exec_()

   def setAlarmTime(self):
      dialog = SetAlarmTimeDialog(self)
      dialog.exec_()

class ChooseAlarmDialog(QDialog, chooseAlarmDialog_ui.Ui_chooseAlarmDialog):
   def __init__(self, parent=None):
      super(ChooseAlarmDialog, self).__init__(parent)
      self.setupUi(self)
      self.openFileDialogButton.clicked.connect(self.chooseFile)
      self.buttonBox.accepted.connect(self.accept)
      self.buttonBox.rejected.connect(self.reject)
      self.alarmSongPath = ""

   def chooseFile(self):
      fileName = QFileDialog.getOpenFileName(self, caption="Wecklied aussuchen", directory=".",filter="Audio files *.mp3 *.ogg *.wav")
      self.pathToFileEdit.setText(fileName)

   def accept(self):
      self.alarmSongPath = self.pathToFileEdit.text()
      QDialog.accept(self)
      
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

class SetAlarmTimeDialog(QDialog, setAlarmTimeDialog_ui.Ui_setAlarmTimeDialog):
   def __init__(self, parent=None):
      super(SetAlarmTimeDialog, self).__init__(parent)
      self.setupUi(self)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = MainWindow()
   main.show()
   app.exec_()
