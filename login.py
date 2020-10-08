# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(551, 365)
        self.label = QtWidgets.QLabel(LoginDialog)
        self.label.setGeometry(QtCore.QRect(60, 100, 191, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 131, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.usernamelineEdit = QtWidgets.QLineEdit(LoginDialog)
        self.usernamelineEdit.setGeometry(QtCore.QRect(320, 110, 161, 31))
        self.usernamelineEdit.setObjectName("usernamelineEdit")
        self.passwordlineEdit = QtWidgets.QLineEdit(LoginDialog)
        self.passwordlineEdit.setGeometry(QtCore.QRect(320, 220, 161, 31))
        self.passwordlineEdit.setObjectName("passwordlineEdit")
        self.loginpushButton = QtWidgets.QPushButton(LoginDialog)
        self.loginpushButton.setGeometry(QtCore.QRect(220, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.loginpushButton.setFont(font)
        self.loginpushButton.setObjectName("loginpushButton")
        self.label_3 = QtWidgets.QLabel(LoginDialog)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Dialog"))
        self.label.setText(_translate("LoginDialog", "用户名"))
        self.label_2.setText(_translate("LoginDialog", "密码"))
        self.loginpushButton.setText(_translate("LoginDialog", "登录"))
        self.label_3.setText(_translate("LoginDialog", "登录"))
