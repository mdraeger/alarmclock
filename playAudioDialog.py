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
from playlistHandler import Playlist, PlaylistHandler

import playAudioDialog_ui

class PlayAudioDialog(QDialog, playAudioDialog_ui.Ui_playAudioDialog):
   def __init__(self, parent=None):
      super(PlayAudioDialog, self).__init__(parent)
      self.setupUi(self)

      self.sleep = False
      self.filelist = []

      # connect signals
      self.sleepModeCheckBox.clicked.connect(self.toggleSleepTimeEdit)
      self.buttonBox.accepted.connect(self.accept)
      self.buttonBox.rejected.connect(self.reject)
      self.listView.clicked.connect(self.setFilelist)

      # setup list view
      self.playlists = PlaylistHandler("playlists.xml").playlists
      model = QStandardItemModel(self.listView)
      for pk in self.playlists:
         item = QStandardItem()
         item.setText(pk)
         item.setEditable(False)
         model.appendRow(item)
      self.listView.setModel(model)


   def toggleSleepTimeEdit(self):
      self.sleepTimeEdit.setEnabled(self.sleepModeCheckBox.isChecked())

   def setFilelist(self, index):
      pk = self.listView.model().data(index)
      self.filelist = self.playlists[pk].filelist()

   def accept(self):
      self.sleep = self.sleepModeCheckBox.isChecked()
      if self.sleep:
         self.sleepTime = self.sleepTimeEdit.time()
      QDialog.accept(self)
