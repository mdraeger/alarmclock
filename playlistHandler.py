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

import os
import sys

import xml.dom
from xml.dom import Node
from xml.dom.minidom import parse

class PlaylistHandler(object):
   def __init__(self, playlistFile):
      self.doc = parse(playlistFile)
      self.playlists = self.__getPlaylists__(self.doc)

   def __getPlaylists__(self, doc):
      playlists = {}
      for p in self.doc.getElementsByTagName("playlist"):
         name = p.getAttribute('name')
         path = p.getAttribute('path')
         isDirectory = p.getAttribute('isDirectory') == 'True'
         if isDirectory:
            playlists[name] = Playlist(name, self.__getFiles__(path))
         else:
            playlists[name] = Playlist(name, ['file://' + path])
      return playlists

   def __getFiles__(self, path):
      files = []
      for file in os.listdir(path):
         if file.endswith(".mp3"):
            files.append('file://' + os.path.join(path, file))
      return sorted(files, key = str.lower)

class Playlist(object):
   def __init__(self, name, filelist):
      self.__name__ = name
      self.__filelist__ = filelist
      
   def name(self):
      return self.__name__

   def filelist(self):
      return self.__filelist__
      
if __name__ == '__main__':
   filename = 'playlists.xml'
   handler = PlaylistHandler(filename)
   for pk in handler.playlists:
      p = handler.playlists[pk]
      print (p.name() + ": " )
      print (p.filelist())
