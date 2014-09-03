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
