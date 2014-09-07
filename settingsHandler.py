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

import xml.dom
from xml.dom import Node
from xml.dom.minidom import parse

import sys

class SettingsHandler(object):
   def __init__(self, settingsFile):
      self.settingsFile = settingsFile
      self.doc = parse(settingsFile)
      self.settings = self.__getSettings__(self.doc)

   def __getSettings__(self, doc):
      settings = {}
      for s in self.doc.getElementsByTagName("setting"):
         settings[s.getAttribute("name")] = s.getAttribute("value")
      return settings

   def set(self, key, value):
      self.settings[key] = value
      for s in self.doc.getElementsByTagName("setting"):
         if s.getAttribute("name") == key:
            s.setAttribute("value", value)
      self.__writeSettings__()
      
   def __writeSettings__(self):
      f=open (self.settingsFile, "wb")
      f.write(self.doc.toprettyxml(newl="", indent="",  encoding="UTF-8"))
      f.close()

if __name__ == '__main__':
   filename = 'settings.xml'
   handler = SettingsHandler(filename)
   handler.set('snooze', '05:00')
   print (handler.settings)
   print (handler.doc.toprettyxml(encoding="UTF-8"))
