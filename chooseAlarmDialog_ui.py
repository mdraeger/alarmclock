# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseAlarmDialog.ui'
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

class Ui_chooseAlarmDialog(object):
    def setupUi(self, chooseAlarmDialog):
        chooseAlarmDialog.setObjectName(_fromUtf8("chooseAlarmDialog"))
        chooseAlarmDialog.resize(262, 116)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chooseAlarmDialog.sizePolicy().hasHeightForWidth())
        chooseAlarmDialog.setSizePolicy(sizePolicy)
        self.pathToFileEdit = QtGui.QLineEdit(chooseAlarmDialog)
        self.pathToFileEdit.setGeometry(QtCore.QRect(20, 40, 201, 20))
        self.pathToFileEdit.setObjectName(_fromUtf8("pathToFileEdit"))
        self.pathToFileLabel = QtGui.QLabel(chooseAlarmDialog)
        self.pathToFileLabel.setGeometry(QtCore.QRect(20, 20, 201, 16))
        self.pathToFileLabel.setObjectName(_fromUtf8("pathToFileLabel"))
        self.buttonBox = QtGui.QDialogButtonBox(chooseAlarmDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 70, 159, 24))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.openFileDialogButton = QtGui.QToolButton(chooseAlarmDialog)
        self.openFileDialogButton.setGeometry(QtCore.QRect(230, 40, 27, 20))
        self.openFileDialogButton.setObjectName(_fromUtf8("openFileDialogButton"))

        self.retranslateUi(chooseAlarmDialog)
        QtCore.QMetaObject.connectSlotsByName(chooseAlarmDialog)

    def retranslateUi(self, chooseAlarmDialog):
        chooseAlarmDialog.setWindowTitle(_translate("chooseAlarmDialog", "Wecklied wählen", None))
        self.pathToFileLabel.setText(_translate("chooseAlarmDialog", "Pfad zu deinem Lieblingslied", None))
        self.openFileDialogButton.setText(_translate("chooseAlarmDialog", "...", None))

