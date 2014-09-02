import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from translate import _translate

import alarmclock_ui
from chooseAlarmDialog import ChooseAlarmDialog
from playAudioDialog import PlayAudioDialog
from setAlarmTimeDialog import SetAlarmTimeDialog
from clockWidget import PyAnalogClock
from myQSlider import MyQSlider

from player import Player

import alarmclock_rc

class MainWindow(QMainWindow, alarmclock_ui.Ui_mainWindow):

   def __init__(self, parent=None):
      super(MainWindow, self).__init__(parent)
      self.setupUi(self)
      self.clockWidget = PyAnalogClock(self.clockFrame)
      self.positionSlider = MyQSlider(self.centralwidget)
      self.positionSlider.setGeometry(QRect(9, 144, 281, 20))
      self.positionSlider.setOrientation(Qt.Horizontal)
      self.positionSlider.setObjectName("positionSlider")

      self.chooseAlarmSoundButton.clicked.connect(self.chooseAlarm)
      self.listenNowButton.clicked.connect(self.playAudio)
      self.changeAlarmTimeButton.clicked.connect(self.setAlarmTime)

      self.alarmTime = QTime()
      self.alarmSongPath = ""

      self.sleepTimer = QTimer(self)
      self.sleepTimer.setSingleShot(True)
      self.sleepTimer.timeout.connect(self.stop)

      self.audioPlayer = None

   def chooseAlarm(self):
      dialog = ChooseAlarmDialog(self)
      if dialog.exec_():
         self.alarmSongPath = dialog.alarmSongPath

   def playAudio(self):
      dialog = PlayAudioDialog(self)
      if dialog.exec_():
         if dialog.sleep:
             rawTime = dialog.sleepTime
             timeToSleep = (rawTime.hour() * 60 + rawTime.minute()) * 60 * 1000
             self.sleepTimer.start(timeToSleep)
         
         self.audioPlayer = Player(self, 'file://' + dialog.filePath)
         # connect the player and button signals
         self.playPauseButton.clicked.connect(self.togglePlayPause)
         self.stopButton.clicked.connect(self.stop)
         self.audioPlayer.currentPositionSignal.connect(self.updateSliderAndStatus)
         self.positionSlider.sliderReleased.connect(self.seek)
         self.positionSlider.clicked.connect(self.seek)
         self.togglePlayPause()

   def seek(self):
      self.audioPlayer.seek(self.positionSlider.value())

   def togglePlayPause(self):
      if self.audioPlayer.playing:
        self.playPauseButton.setIcon(QIcon(":/icons/control-play-icon.png"))
      else:
        self.playPauseButton.setIcon(QIcon(":/icons/control-pause-icon.png"))
      self.audioPlayer.togglePlayPause()
   
   def stop(self):
      self.playPauseButton.setIcon(QIcon(":/icons/control-play-icon.png"))
      if self.audioPlayer == None:
         pass
      elif self.audioPlayer.playing:
         self.audioPlayer.stop()

   def updateSliderAndStatus(self, currentPosition, duration):
      self.positionSlider.setRange(0,duration)
      self.positionSlider.setSliderPosition(currentPosition)
      self.updateStatusBar("%d:%02d / %d:%02d" % (currentPosition/60, currentPosition %60, duration /60, duration % 60))

   def updateStatusBar(self, text):
      self.statusbar.showMessage(text)

   def setAlarmTime(self):
      dialog = SetAlarmTimeDialog(self)
      dialog.exec_()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = MainWindow()
   main.show()
   app.exec_()
