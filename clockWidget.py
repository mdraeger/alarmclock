from PyQt4 import QtCore, QtGui

class PyAnalogClock(QtGui.QWidget):
   """PyAnalogClock(QtGui.QWidget)

   provides an analog clock custom widget with signals, slots and properties.
   The implementation is based on the Analog Clock example provided with both Qt and PyQt.
   """

   timeChanged = QtCore.pyqtSignal(QtCore.QTime)
   timeZoneChanged = QtCore.pyqtSignal(int)

   def __init__(self, parent=None):
      super(PyAnalogClock, self).__init__(parent)
      
      self.timeZoneOffset = 0
      timer = QtCore.QTimer(self)
      timer.timeout.connect(self.update)
      timer.timeout.connect(self.updateTime)
      timer.start(1000)

      self.setWindowTitle(QtCore.QObject.tr(self, "Analog Clock"))
      self.resize(120,120)

      self.hourHand = QtGui.QPolygon([
         QtCore.QPoint(7,8),
         QtCore.QPoint(-7,8),
         QtCore.QPoint(0,-30)
      ])

      self.minuteHand = QtGui.QPolygon([
         QtCore.QPoint(7,8),
         QtCore.QPoint(-7,8),
         QtCore.QPoint(0,-50)
      ])

      self.hourColor = QtGui.QColor(0,127,0)
      self.minuteColor = QtGui.QColor(0,127,127,191)

   def paintEvent(self, event):
      side = min(self.width(), self.height())
      time = QtCore.QTime.currentTime()
      time = time.addSecs(self.timeZoneOffset * 3600)

      painter = QtGui.QPainter()
      painter.begin(self)
      painter.setRenderHint(QtGui.QPainter.Antialiasing)
      painter.translate(self.width() / 2, self.height() / 2)
      painter.scale(side / 120.0, side / 120.0)

      painter.setPen(QtCore.Qt.NoPen)
      painter.setBrush(QtGui.QBrush(self.hourColor))

      painter.save()
      painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
      painter.drawConvexPolygon(self.hourHand)
      painter.restore()

      painter.setPen(self.hourColor)

      for i in range(0,12):
         painter.drawLine(50,0,58,0)
         painter.rotate(30.0)

      painter.setPen(QtCore.Qt.NoPen)
      painter.setBrush(QtGui.QBrush(self.minuteColor))

      painter.save()
      painter.rotate(6.0 * ((time.minute() + time.second() / 60.0)))
      painter.drawConvexPolygon(self.minuteHand)
      painter.restore()

      painter.setPen(self.minuteColor)

      for j in range(0,60):
         if j % 5 != 0:
            painter.drawLine(55,0,58,0)
         painter.rotate(6.0)

      painter.end()

   def minimumSizeHint(self):
      return QtCore.QSize(50,50)

   def sizeHint(self):
      return QtCore.QSize(100,100)

   def updateTime(self):
      self.timeChanged.emit(QtCore.QTime.currentTime())

   def getTimeZone(self):
      return self.timeZoneOffset

   @QtCore.pyqtSlot(int)
   def setTimeZone(self,value):
      self.timeZoneOffset = value
      self.timeZoneChanged.emit(value)
      self.update()

   def resetTimeZone(self):
      self.timeZoneOffset = 0
      self.timeZoneChanged.emit(0)
      self.update()

   timeZone = QtCore.pyqtProperty(int, getTimeZone, setTimeZone, resetTimeZone)

if __name__ == "__main__":
   import sys

   app = QtGui.QApplication(sys.argv)
   clock = PyAnalogClock()
   clock.show()
   sys.exit(app.exec_())
