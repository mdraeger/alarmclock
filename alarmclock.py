import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from translate import _translate

import alarmclock_ui
from chooseAlarmDialog import ChooseAlarmDialog
from playAudioDialog import PlayAudioDialog
from setAlarmTimeDialog import SetAlarmTimeDialog
import clockWidget

import player

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

      self.audioPlayer = None

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

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = MainWindow()
   main.show()
   app.exec_()
