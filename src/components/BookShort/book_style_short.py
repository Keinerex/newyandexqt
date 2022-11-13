# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_style_short.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from src.components.Star.star import Star


class Ui_Form(object):
    def setupUi(self, Form, title, authors, genre, price, rate):
        self.frame = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
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
        self.book_btn = QtWidgets.QPushButton(self.frame)
        self.book_btn.setGeometry(QtCore.QRect(20, 16, 551, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.book_btn.setFont(font)
        self.book_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.book_btn.setStyleSheet("text-align: left;\n"
                                    "background: #ffffff")
        self.book_btn.setObjectName("book_btn")
        self.author = QtWidgets.QLabel(self.frame)
        self.author.setGeometry(QtCore.QRect(20, 65, 531, 22))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.author.setFont(font)
        self.author.setStyleSheet("font-style: normal;\n"
                                  "font-weight: 400;\n"
                                  "font-size: 16px;\n"
                                  "color: rgba(0, 0, 0, 0.5);")
        self.author.setObjectName("author")
        self.genre = QtWidgets.QLabel(self.frame)
        self.genre.setGeometry(QtCore.QRect(20, 95, 531, 22))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.genre.setFont(font)
        self.genre.setStyleSheet("font-style: normal;\n"
                                 "font-weight: 400;\n"
                                 "font-size: 16px;\n"
                                 "color: rgba(0, 0, 0, 0.5);")
        self.genre.setObjectName("genre")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 125, 110, 16))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 110, 16))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.stars = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.stars.setContentsMargins(0, 0, 0, 0)
        self.stars.setObjectName("starts")
        self.price = QtWidgets.QLabel(self.frame)
        self.price.setGeometry(QtCore.QRect(20, 163, 200, 33))
        self.price.setStyleSheet("font-style: normal;\n"
                                 "font-weight: 700;\n"
                                 "font-size: 24px;")
        self.price.setObjectName("price")
        self.retranslateUi(Form, title, authors, genre, price, rate)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, title, authors, genre, price, rate):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.book_btn.setText(_translate("Form", title))
        self.author.setText(_translate("Form", ", ".join(authors)))
        self.genre.setText(_translate("Form", genre))
        self.price.setText(_translate("Form", f"{price}P"))
        self.draw_rate(Form, rate)

    def draw_rate(self, Form, rate):
        for i in reversed(range(self.stars.count())):
            self.stars.takeAt(i).widget().setParent(None)
        for i in range(rate):
            self.stars.addWidget(Star(Form, type="fill"))
        for i in range(5 - rate):
            self.stars.addWidget(Star(Form))

