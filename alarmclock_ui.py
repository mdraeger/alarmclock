# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarmclock.ui'
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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(300, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"    background: transparent;\n"
"    border-image: url(:/wallpapers/girly-pink.jpg);\n"
"    background-repeat: none;\n"
"}\n"
"\n"
"QFrame {\n"
"    border: none;\n"
"}\n"
"\n"
"QToolButton {\n"
"    border: none;\n"
"}"))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.backwardButton = QtGui.QToolButton(self.centralwidget)
        self.backwardButton.setGeometry(QtCore.QRect(80, 150, 16, 16))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/control-rewind-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backwardButton.setIcon(icon)
        self.backwardButton.setObjectName(_fromUtf8("backwardButton"))
        self.incVolumeButton = QtGui.QToolButton(self.centralwidget)
        self.incVolumeButton.setGeometry(QtCore.QRect(230, 150, 16, 16))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/speaker-volume-control-up-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.incVolumeButton.setIcon(icon1)
        self.incVolumeButton.setObjectName(_fromUtf8("incVolumeButton"))
        self.decVolumeButton = QtGui.QToolButton(self.centralwidget)
        self.decVolumeButton.setGeometry(QtCore.QRect(210, 150, 16, 16))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/speaker-volume-control-down-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.decVolumeButton.setIcon(icon2)
        self.decVolumeButton.setObjectName(_fromUtf8("decVolumeButton"))
        self.playPauseButton = QtGui.QToolButton(self.centralwidget)
        self.playPauseButton.setGeometry(QtCore.QRect(100, 150, 16, 16))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/control-play-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playPauseButton.setIcon(icon3)
        self.playPauseButton.setObjectName(_fromUtf8("playPauseButton"))
        self.stopButton = QtGui.QToolButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(120, 150, 16, 16))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/control-stop-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon4)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.forwardButton = QtGui.QToolButton(self.centralwidget)
        self.forwardButton.setGeometry(QtCore.QRect(140, 150, 16, 16))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/control-fastforward-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forwardButton.setIcon(icon5)
        self.forwardButton.setObjectName(_fromUtf8("forwardButton"))
        self.chooseAlarmSoundButton = QtGui.QToolButton(self.centralwidget)
        self.chooseAlarmSoundButton.setGeometry(QtCore.QRect(10, 5, 32, 32))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Music-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chooseAlarmSoundButton.setIcon(icon6)
        self.chooseAlarmSoundButton.setIconSize(QtCore.QSize(48, 48))
        self.chooseAlarmSoundButton.setObjectName(_fromUtf8("chooseAlarmSoundButton"))
        self.toggleAlarmOnOffButton = QtGui.QToolButton(self.centralwidget)
        self.toggleAlarmOnOffButton.setGeometry(QtCore.QRect(260, 85, 32, 32))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Alarm-clock-disabled-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleAlarmOnOffButton.setIcon(icon7)
        self.toggleAlarmOnOffButton.setIconSize(QtCore.QSize(48, 48))
        self.toggleAlarmOnOffButton.setObjectName(_fromUtf8("toggleAlarmOnOffButton"))
        self.changeAlarmTimeButton = QtGui.QToolButton(self.centralwidget)
        self.changeAlarmTimeButton.setGeometry(QtCore.QRect(260, 5, 32, 32))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/time-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeAlarmTimeButton.setIcon(icon8)
        self.changeAlarmTimeButton.setIconSize(QtCore.QSize(48, 48))
        self.changeAlarmTimeButton.setObjectName(_fromUtf8("changeAlarmTimeButton"))
        self.listenNowButton = QtGui.QToolButton(self.centralwidget)
        self.listenNowButton.setGeometry(QtCore.QRect(10, 75, 32, 32))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Music-Piano-Chello-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.listenNowButton.setIcon(icon9)
        self.listenNowButton.setIconSize(QtCore.QSize(48, 48))
        self.listenNowButton.setObjectName(_fromUtf8("listenNowButton"))
        self.clockFrame = QtGui.QFrame(self.centralwidget)
        self.clockFrame.setGeometry(QtCore.QRect(90, 5, 121, 121))
        self.clockFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.clockFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.clockFrame.setObjectName(_fromUtf8("clockFrame"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Pi Alarm !", None))
        self.backwardButton.setText(_translate("mainWindow", "...", None))
        self.incVolumeButton.setText(_translate("mainWindow", "...", None))
        self.decVolumeButton.setText(_translate("mainWindow", "...", None))
        self.playPauseButton.setText(_translate("mainWindow", "...", None))
        self.stopButton.setText(_translate("mainWindow", "...", None))
        self.forwardButton.setText(_translate("mainWindow", "...", None))
        self.chooseAlarmSoundButton.setText(_translate("mainWindow", "...", None))
        self.toggleAlarmOnOffButton.setText(_translate("mainWindow", "...", None))
        self.changeAlarmTimeButton.setText(_translate("mainWindow", "...", None))
        self.listenNowButton.setText(_translate("mainWindow", "...", None))

import alarmclock_rc
