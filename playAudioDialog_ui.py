# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playAudioDialog.ui'
#
# Created: Sat Sep  6 22:16:45 2014
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_playAudioDialog(object):
    def setupUi(self, playAudioDialog):
        playAudioDialog.setObjectName(_fromUtf8("playAudioDialog"))
        playAudioDialog.resize(271, 166)
        self.label = QtGui.QLabel(playAudioDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(playAudioDialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 201, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.toolButton = QtGui.QToolButton(playAudioDialog)
        self.toolButton.setGeometry(QtCore.QRect(230, 40, 27, 20))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.sleepModeCheckBox = QtGui.QCheckBox(playAudioDialog)
        self.sleepModeCheckBox.setGeometry(QtCore.QRect(150, 77, 111, 19))
        self.sleepModeCheckBox.setObjectName(_fromUtf8("sleepModeCheckBox"))
        self.sleepTimeEdit = QtGui.QTimeEdit(playAudioDialog)
        self.sleepTimeEdit.setEnabled(False)
        self.sleepTimeEdit.setGeometry(QtCore.QRect(20, 80, 118, 22))
        self.sleepTimeEdit.setTime(QtCore.QTime(1, 0, 0))
        self.sleepTimeEdit.setObjectName(_fromUtf8("sleepTimeEdit"))
        self.buttonBox = QtGui.QDialogButtonBox(playAudioDialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 120, 159, 24))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(playAudioDialog)
        QtCore.QMetaObject.connectSlotsByName(playAudioDialog)

    def retranslateUi(self, playAudioDialog):
        playAudioDialog.setWindowTitle(_translate("playAudioDialog", "Lied/ Album hören", None))
        self.label.setText(_translate("playAudioDialog", "Wähle, was du jetzt hören möchtest.", None))
        self.toolButton.setText(_translate("playAudioDialog", "...", None))
        self.sleepModeCheckBox.setText(_translate("playAudioDialog", "Schlafmodus?", None))

