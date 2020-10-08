# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chatMainWindow(object):
    def setupUi(self, chatMainWindow):
        chatMainWindow.setObjectName("chatMainWindow")
        chatMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(chatMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chattextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.chattextBrowser.setGeometry(QtCore.QRect(0, 0, 801, 361))
        self.chattextBrowser.setObjectName("chattextBrowser")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(0, 360, 801, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.inputtextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.inputtextEdit.setGeometry(QtCore.QRect(0, 380, 511, 181))
        self.inputtextEdit.setObjectName("inputtextEdit")
        self.sendpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendpushButton.setGeometry(QtCore.QRect(520, 380, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.sendpushButton.setFont(font)
        self.sendpushButton.setObjectName("sendpushButton")
        chatMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chatMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        chatMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(chatMainWindow)
        self.statusbar.setObjectName("statusbar")
        chatMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(chatMainWindow)
        QtCore.QMetaObject.connectSlotsByName(chatMainWindow)

    def retranslateUi(self, chatMainWindow):
        _translate = QtCore.QCoreApplication.translate
        chatMainWindow.setWindowTitle(_translate("chatMainWindow", "MainWindow"))
        self.sendpushButton.setText(_translate("chatMainWindow", "发送"))
