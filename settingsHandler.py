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
