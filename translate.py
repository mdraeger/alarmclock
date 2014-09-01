import sys

from PyQt4.QtGui import QApplication

try:
   _encoding = QApplication.UnicodeUTF8
   def _translate(context, text, disambig):
      return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
       return QApplication.translate(context, text, disambig)
