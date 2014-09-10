# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarmHandleDialog.ui'
#
# Created: Wed Sep 10 18:11:41 2014
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

class Ui_alarmHandleDialog(object):
    def setupUi(self, alarmHandleDialog):
        alarmHandleDialog.setObjectName(_fromUtf8("alarmHandleDialog"))
        alarmHandleDialog.resize(129, 69)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(alarmHandleDialog.sizePolicy().hasHeightForWidth())
        alarmHandleDialog.setSizePolicy(sizePolicy)
        alarmHandleDialog.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        alarmHandleDialog.setStyleSheet(_fromUtf8("QToolButton {\n"
"background: transparent;\n"
"}"))
        self.alarmOffButton = QtGui.QToolButton(alarmHandleDialog)
        self.alarmOffButton.setGeometry(QtCore.QRect(10, 10, 48, 48))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Cute-Ball-Stop-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alarmOffButton.setIcon(icon)
        self.alarmOffButton.setIconSize(QtCore.QSize(48, 48))
        self.alarmOffButton.setObjectName(_fromUtf8("alarmOffButton"))
        self.snoozeButton = QtGui.QToolButton(alarmHandleDialog)
        self.snoozeButton.setGeometry(QtCore.QRect(70, 10, 48, 48))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Adium-Bird-Sleep-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snoozeButton.setIcon(icon1)
        self.snoozeButton.setIconSize(QtCore.QSize(48, 48))
        self.snoozeButton.setObjectName(_fromUtf8("snoozeButton"))

        self.retranslateUi(alarmHandleDialog)
        QtCore.QMetaObject.connectSlotsByName(alarmHandleDialog)

    def retranslateUi(self, alarmHandleDialog):
        alarmHandleDialog.setWindowTitle(_translate("alarmHandleDialog", "AUFSTEHEN!!!", None))
        self.alarmOffButton.setText(_translate("alarmHandleDialog", "...", None))
        self.snoozeButton.setText(_translate("alarmHandleDialog", "...", None))

import alarmclock_rc
