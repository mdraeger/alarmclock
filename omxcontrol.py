import os
from subprocess import Popen, PIPE

class OMXControl:
   def __init__():
      self.running = False
      self.omxProcess = None
   
   def start(filepath):
      if not self.running:
         self.omxProcess = Popen(['omxplayer', filepath], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)

   def __sendKey__(self,key):
      if self.running:
         self.omxProcess.stdin.write(key)
         self.omxProcess.stdin.flush()

   def __queryKey__(self,key):
      if self.running:
         self.omxProcess.stdin.write(key)
         self.omxProcess.stdin.flush()
         proc_read = self.omxProcess.stdout.readline()
         if proc_read:
            return (proc_read)
         else:
            return (None)
      else:
         return(None)

   def incVolume(self):
      self.__sendKey__('+')

   def decVolume(self):
      self.__sendKey__('-')
