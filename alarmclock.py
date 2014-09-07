#!/usr/bin/env python3

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

from translate import _translate

import alarmclock_ui
from chooseAlarmDialog import ChooseAlarmDialog
from playAudioDialog import PlayAudioDialog
from setAlarmTimeDialog import SetAlarmTimeDialog
from alarmHandleDialog import AlarmHandleDialog 
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

      # handle alarm
      self.alarmHandleDialog = AlarmHandleDialog(self)
      self.alarmHandleDialog.alarmOffButton.clicked.connect(self.stopAlarm)
      self.alarmHandleDialog.snoozeButton.clicked.connect(self.snoozeAlarm)
      self.alarmHandleDialog.hide()

      # audio player elements
      self.audioPlayer = Player(self)
      # connect the player and button signals
      self.playPauseButton.clicked.connect(self.audioPlayer.togglePlayPause)
      self.stopButton.clicked.connect(self.stop)
      self.audioPlayer.currentPositionSignal.connect(self.updateSliderAndStatus)
      self.backwardButton.clicked.connect(self.audioPlayer.lastTitle)
      self.forwardButton.clicked.connect(self.audioPlayer.nextTitle)
      self.incVolumeButton.clicked.connect(self.audioPlayer.incVolume)
      self.decVolumeButton.clicked.connect(self.audioPlayer.decVolume)
      self.audioPlayer.currentStateSignal.connect(self.updatePlayButton)
      self.audioPlayer.currentSongArtistTitleSignal.connect(self.updateArtistTitle)
      self.positionSlider.sliderReleased.connect(self.seek)
      self.positionSlider.clicked.connect(self.seek)
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
         self.toggleAlarmOnOffButton.setIcon(QIcon(":/icons/Alarm-clock-disabled-icon.png"))
      else:
         timeTillNextAlarm = (ONEDAYMSEC + QTime.currentTime().msecsTo(self.alarmTime)) % ONEDAYMSEC
         self.alarmTimer.start(timeTillNextAlarm)
         self.alarmActive = True
         self.toggleAlarmOnOffButton.setIcon(QIcon(":/icons/Alarm-clock-icon.png"))
      self.updateStatusBar("")

   def playAlarm(self):
      self.stop() # just in case ...
      self.audioPlayer.setFileList([self.alarmSongPath])
      self.alarmHandleDialog.show()

   def stopAlarm(self):
      self.stop()
      self.alarmHandleDialog.hide()
      self.toggleAlarmOnOff()
      self.toggleAlarmOnOff()

   def snoozeAlarm(self):
      pass

   def playAudio(self):
      self.stop() # just in case ...
      dialog = PlayAudioDialog(self)
      if dialog.exec_():
         if dialog.sleep:
             rawTime = dialog.sleepTime
             timeToSleep = (rawTime.hour() * 60 + rawTime.minute()) * 60 * 1000
             self.sleepTimer.start(timeToSleep)
         self.audioPlayer.setFileList(dialog.filelist)

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
      else:
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
