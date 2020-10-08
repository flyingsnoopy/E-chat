# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addfriend.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addfriendDialog(object):
    def setupUi(self, addfriendDialog):
        addfriendDialog.setObjectName("addfriendDialog")
        addfriendDialog.resize(551, 365)
        self.label = QtWidgets.QLabel(addfriendDialog)
        self.label.setGeometry(QtCore.QRect(60, 100, 191, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addfriendDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 211, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.friendnamelineEdit = QtWidgets.QLineEdit(addfriendDialog)
        self.friendnamelineEdit.setGeometry(QtCore.QRect(320, 110, 161, 31))
        self.friendnamelineEdit.setObjectName("friendnamelineEdit")
        self.friendaddresslineEdit = QtWidgets.QLineEdit(addfriendDialog)
        self.friendaddresslineEdit.setGeometry(QtCore.QRect(320, 220, 161, 31))
        self.friendaddresslineEdit.setObjectName("friendaddresslineEdit")
        self.appearButton = QtWidgets.QPushButton(addfriendDialog)
        self.appearButton.setGeometry(QtCore.QRect(220, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.appearButton.setFont(font)
        self.appearButton.setObjectName("appearButton")
        self.label_3 = QtWidgets.QLabel(addfriendDialog)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(addfriendDialog)
        QtCore.QMetaObject.connectSlotsByName(addfriendDialog)

    def retranslateUi(self, addfriendDialog):
        _translate = QtCore.QCoreApplication.translate
        addfriendDialog.setWindowTitle(_translate("addfriendDialog", "Dialog"))
        self.label.setText(_translate("addfriendDialog", "好友名"))
        self.label_2.setText(_translate("addfriendDialog", "好友地址"))
        self.appearButton.setText(_translate("addfriendDialog", "添加"))
        self.label_3.setText(_translate("addfriendDialog", "添加好友"))
