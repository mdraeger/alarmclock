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

from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QSlider

class MyQSlider(QSlider):
   clicked = pyqtSignal()

   def __init__(self, parent=None):
      super(MyQSlider, self).__init__(parent)
        
   def mousePressEvent(self, event):
      if event.button() == Qt.LeftButton:
         if self.orientation == Qt.Vertical:
            self.setValue(self.minimum() + ((self.maximum() - self.minimum()) * (self.height() - event.y())) / self.height() )
         else:
            self.setValue(self.minimum() + ((self.maximum() - self.minimum()) * event.x()) / self.width()) 
         event.accept

      self.clicked.emit()
      QSlider.mousePressEvent(self, event)
