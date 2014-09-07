#!/usr/bin/env python3
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
from settingsHandler import SettingsHandler

import alarmclock_rc

ONEDAYMSEC = 24*60*60*1000

class MainWindow(QMainWindow, alarmclock_ui.Ui_mainWindow):

   def __init__(self, parent=None):
      super(MainWindow, self).__init__(parent)

      # settings from xml
      self.settingsHandler = SettingsHandler('settings.xml')

      # set up gui elements
      self.setupUi(self)
      self.clockWidget = PyAnalogClock(self.clockFrame)
      self.positionSlider = MyQSlider(self.centralwidget)
      self.positionSlider.setGeometry(QRect(9, 144, 281, 20))
      self.positionSlider.setOrientation(Qt.Horizontal)
      self.positionSlider.setObjectName("positionSlider")

      # connect signals
      self.chooseAlarmSoundButton.clicked.connect(self.chooseAlarm)
      self.listenNowButton.clicked.connect(self.playAudio)
      self.changeAlarmTimeButton.clicked.connect(self.setAlarmTime)
      self.toggleAlarmOnOffButton.clicked.connect(self.toggleAlarmOnOff)

      # sleep timer setup
      self.sleepTimer = QTimer(self)
      self.sleepTimer.setSingleShot(True)
      self.sleepTimer.timeout.connect(self.stop)

      # alarm time setup
      self.alarmActive = False
      self.alarmTime = QTime.fromString(self.settingsHandler.settings['alarmtime'],'hh:mm')
      self.alarmSongPath = self.settingsHandler.settings['alarmsong']
      self.snoozeTime = QTime.fromString(self.settingsHandler.settings['snooze'], 'mm:ss')
      self.alarmTimer = QTimer()
      self.alarmTimer.setSingleShot(True)
      self.alarmTimer.timeout.connect(self.playAlarm)

      # audio player elements
      self.audioPlayer = None
      self.currentArtistTitle = ""

      # set status
      self.updateStatusBar("")

   def chooseAlarm(self):
      dialog = ChooseAlarmDialog(self.alarmSongPath, self)
      if dialog.exec_():
         self.alarmSongPath = dialog.alarmSongPath
         self.settingsHandler.set('alarmsong', 'file://' + self.alarmSongPath)

   def toggleAlarmOnOff(self):
      if self.alarmActive:
         self.alarmTimer.stop()
         self.alarmActive = False
      else:
         timeTillNextAlarm = (ONEDAYMSEC + QTime.currentTime().msecsTo(self.alarmTime)) % ONEDAYMSEC
         self.alarmTimer.start(timeTillNextAlarm)
         self.alarmActive = True
      self.updateStatusBar("")

   def playAlarm(self):
      self.setupAndStartPlayer([self.alarmSongPath])

   def playAudio(self):
      dialog = PlayAudioDialog(self)
      if dialog.exec_():
         if dialog.sleep:
             rawTime = dialog.sleepTime
             timeToSleep = (rawTime.hour() * 60 + rawTime.minute()) * 60 * 1000
             self.sleepTimer.start(timeToSleep)
         self.setupAndStartPlayer(['file://' + dialog.filePath])

   def setupAndStartPlayer(self, files):
      self.audioPlayer = Player(self, files)
      # connect the player and button signals
      self.playPauseButton.clicked.connect(self.audioPlayer.togglePlayPause)
      self.stopButton.clicked.connect(self.stop)
      self.audioPlayer.currentPositionSignal.connect(self.updateSliderAndStatus)
      self.incVolumeButton.clicked.connect(self.audioPlayer.incVolume)
      self.decVolumeButton.clicked.connect(self.audioPlayer.decVolume)
      self.audioPlayer.currentStateSignal.connect(self.updatePlayButton)
      self.audioPlayer.currentSongArtistTitleSignal.connect(self.updateArtistTitle)
      self.positionSlider.sliderReleased.connect(self.seek)
      self.positionSlider.clicked.connect(self.seek)

   def seek(self):
      self.audioPlayer.seek(self.positionSlider.value())

   def updatePlayButton(self, playerState):
      if playerState:
        self.playPauseButton.setIcon(QIcon(":/icons/control-pause-icon.png"))
      else:
        self.playPauseButton.setIcon(QIcon(":/icons/control-play-icon.png"))

   def updateArtistTitle(self, artistTitle):
      self.currentArtistTitle = artistTitle
   
   def stop(self):
      self.playPauseButton.setIcon(QIcon(":/icons/control-play-icon.png"))
      if self.audioPlayer == None:
         pass
      elif self.audioPlayer.playing:
         self.audioPlayer.stop()

   def updateSliderAndStatus(self, currentPosition, duration):
      self.positionSlider.setRange(0,duration)
      self.positionSlider.setSliderPosition(currentPosition)
      self.updateStatusBar("%s, %d:%02d / %d:%02d" % (self.currentArtistTitle, currentPosition/60, currentPosition %60, duration /60, duration % 60))

   def updateStatusBar(self, text):
      alarmInfo = "Wecker: "
      if self.alarmActive:
         alarmInfo += self.alarmTime.toString("hh:mm") + "; "
      else:
         alarmInfo += "aus; "
      self.statusbar.showMessage(alarmInfo + text)

   def setAlarmTime(self):
      dialog = SetAlarmTimeDialog(self.alarmTime, self)
      if dialog.exec_():
         self.alarmTime = dialog.alarmTime
         self.settingsHandler.set('alarmtime', self.alarmTime.toString("hh:mm"))
         self.toggleAlarmOnOff()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = MainWindow()
   main.show()
   app.exec_()
