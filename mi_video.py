# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mi_video.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1103, 850)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/player.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoPlayer.sizePolicy().hasHeightForWidth())
        self.videoPlayer.setSizePolicy(sizePolicy)
        self.videoPlayer.setMaximumSize(QtCore.QSize(2000, 1000))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.verticalLayout.addWidget(self.videoPlayer)
        self.seekSlider = phonon.Phonon.SeekSlider(self.centralwidget)
        self.seekSlider.setMaximumSize(QtCore.QSize(2000, 50))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.verticalLayout.addWidget(self.seekSlider)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(2000, 50))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.frame)
        self.volumeSlider.setMaximumSize(QtCore.QSize(400, 50))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.horizontalLayout.addWidget(self.volumeSlider)
        self.play_PB = QtGui.QPushButton(self.frame)
        self.play_PB.setMaximumSize(QtCore.QSize(2000, 50))
        self.play_PB.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_PB.setIcon(icon1)
        self.play_PB.setObjectName(_fromUtf8("play_PB"))
        self.horizontalLayout.addWidget(self.play_PB)
        self.pause_PB = QtGui.QPushButton(self.frame)
        self.pause_PB.setMaximumSize(QtCore.QSize(2000, 50))
        self.pause_PB.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_PB.setIcon(icon2)
        self.pause_PB.setObjectName(_fromUtf8("pause_PB"))
        self.horizontalLayout.addWidget(self.pause_PB)
        self.stop_PB = QtGui.QPushButton(self.frame)
        self.stop_PB.setMaximumSize(QtCore.QSize(2000, 50))
        self.stop_PB.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_PB.setIcon(icon3)
        self.stop_PB.setObjectName(_fromUtf8("stop_PB"))
        self.horizontalLayout.addWidget(self.stop_PB)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))

from PyQt4 import phonon
import icons_rc
