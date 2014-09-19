# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setAlarmTimeDialog.ui'
#
# Created: Fri Sep 19 10:35:45 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_setAlarmTimeDialog(object):
    def setupUi(self, setAlarmTimeDialog):
        setAlarmTimeDialog.setObjectName(_fromUtf8("setAlarmTimeDialog"))
        setAlarmTimeDialog.resize(181, 135)
        self.timeEdit = QtGui.QTimeEdit(setAlarmTimeDialog)
        self.timeEdit.setGeometry(QtCore.QRect(10, 50, 159, 22))
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.buttonBox = QtGui.QDialogButtonBox(setAlarmTimeDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 90, 159, 24))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(setAlarmTimeDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(setAlarmTimeDialog)
        QtCore.QMetaObject.connectSlotsByName(setAlarmTimeDialog)

    def retranslateUi(self, setAlarmTimeDialog):
        setAlarmTimeDialog.setWindowTitle(_translate("setAlarmTimeDialog", "Weckzeit einstellen", None))
        self.label.setText(_translate("setAlarmTimeDialog", "Wann willst du wach werden?", None))

