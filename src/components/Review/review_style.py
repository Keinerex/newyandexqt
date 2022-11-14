# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'review_style.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from src.components.Star.star import Star


class Ui_Form(object):
    def setupUi(self, Form, user, text, rate):
        Form.setObjectName("Form")
        Form.resize(1200, 200)
        Form.setMinimumSize(1200, 200)
        Form.setGeometry(QtCore.QRect(50, 0, 1200, 200))
        Form.setMinimumSize(1100, 200)
        Form.setStyleSheet("background: #FFFFFF; border-radius: 8px;")
        Form.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Form.setFrameShadow(QtWidgets.QFrame.Raised)
        Form.setObjectName("frame")
        self.author = QtWidgets.QLabel(Form)
        self.author.setGeometry(QtCore.QRect(40, 20, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.author.setFont(font)
        self.author.setObjectName("author")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text = QtWidgets.QTextBrowser(Form)
        self.text.setGeometry(QtCore.QRect(40, 50, 1000, 150))
        self.text.setFont(font)
        self.text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text.setObjectName("text")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1040, 25, 120, 16))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.stars = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.stars.setContentsMargins(0, 0, 0, 0)
        self.stars.setObjectName("starts")

        self.retranslateUi(Form, user, text, rate)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, user, text, rate):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.author.setText(_translate("Form", user))
        self.text.setText(text)
        for i in range(rate):
            self.stars.addWidget(Star(Form, star_type="fill"))
        for i in range(5 - rate):
            self.stars.addWidget(Star(Form))
