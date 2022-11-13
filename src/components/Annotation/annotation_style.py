# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'annotation_style.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(590, 220)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 590, 220))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.frame.setFont(font)
        self.frame.setTabletTracking(False)
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background: #ffffff;\n"
"border-radius: 8px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.annotation = QtWidgets.QPushButton(self.frame)
        self.annotation.setGeometry(QtCore.QRect(20, 16, 551, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.annotation.setFont(font)
        self.annotation.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.annotation.setStyleSheet("text-align: left;\n"
"background: #ffffff")
        self.annotation.setObjectName("annotation")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(30, 50, 541, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.annotation.setText(_translate("Form", "Аннотация"))

    def setAnnotation(self, text):
        self.textBrowser.setText(text)