# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'if_calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfCalc(object):
    def setupUi(self, InfCalc):
        InfCalc.setObjectName("InfCalc")
        InfCalc.resize(757, 612)
        self.centralwidget = QtWidgets.QWidget(InfCalc)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 744, 554))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(296, 35))
        self.lineEdit.setMaximumSize(QtCore.QSize(296, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(221, 238, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setMaximumSize(QtCore.QSize(100, 25))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("background-color: rgb(221, 238, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setMaximumSize(QtCore.QSize(100, 25))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.setStyleSheet("background-color: rgb(175, 218, 222);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(9, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(10, "")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(138, 206, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background-color: rgb(175, 218, 222);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_2.addWidget(self.textBrowser_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(373, 35))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(11224, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(221, 238, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(230, 30))
        self.textBrowser.setStyleSheet("background-color: rgb(175, 218, 222);")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_3.setMaximumSize(QtCore.QSize(100, 25))
        self.comboBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_3.setStyleSheet("background-color: rgb(175, 218, 222);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(9, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(10, "")
        self.gridLayout_2.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_4.setMaximumSize(QtCore.QSize(100, 25))
        self.comboBox_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_4.setStyleSheet("background-color: rgb(175, 218, 222);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(10, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(11, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(12, "")
        self.gridLayout_2.addWidget(self.comboBox_4, 1, 1, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_4.setMaximumSize(QtCore.QSize(230, 30))
        self.textBrowser_4.setStyleSheet("background-color: rgb(175, 218, 222);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout_2.addWidget(self.textBrowser_4, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(138, 206, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_3.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background-color: rgb(175, 218, 222);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout.addWidget(self.textBrowser_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(296, 35))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100000, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(221, 238, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_5 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_5.setMaximumSize(QtCore.QSize(100, 25))
        self.comboBox_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_5.setStyleSheet("background-color: rgb(221, 238, 255);")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_5, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 1, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_7.setMaximumSize(QtCore.QSize(100, 25))
        self.comboBox_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_7.setStyleSheet("background-color: rgb(175, 218, 222);")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_7, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(138, 206, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_5.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setStyleSheet("background-color: rgb(175, 218, 222);")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_3.addWidget(self.textBrowser_5)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_3)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowser_6.setMinimumSize(QtCore.QSize(300, 0))
        self.textBrowser_6.setMaximumSize(QtCore.QSize(296, 16777215))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.textBrowser_6)
        InfCalc.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InfCalc)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 26))
        self.menubar.setObjectName("menubar")
        InfCalc.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InfCalc)
        self.statusbar.setObjectName("statusbar")
        InfCalc.setStatusBar(self.statusbar)

        self.retranslateUi(InfCalc)
        QtCore.QMetaObject.connectSlotsByName(InfCalc)

    def retranslateUi(self, InfCalc):
        _translate = QtCore.QCoreApplication.translate
        InfCalc.setWindowTitle(_translate("InfCalc", "Информатика"))
        self.label_4.setText(_translate("InfCalc", "Переводчик из одной СС в другую СС:"))
        self.label.setText(_translate("InfCalc", "Исходное число:"))
        self.comboBox.setItemText(0, _translate("InfCalc", "10"))
        self.comboBox.setItemText(1, _translate("InfCalc", "9"))
        self.comboBox.setItemText(2, _translate("InfCalc", "8"))
        self.comboBox.setItemText(3, _translate("InfCalc", "7"))
        self.comboBox.setItemText(4, _translate("InfCalc", "6"))
        self.comboBox.setItemText(5, _translate("InfCalc", "5"))
        self.comboBox.setItemText(6, _translate("InfCalc", "4"))
        self.comboBox.setItemText(7, _translate("InfCalc", "3"))
        self.comboBox.setItemText(8, _translate("InfCalc", "2"))
        self.comboBox_2.setItemText(0, _translate("InfCalc", "2"))
        self.comboBox_2.setItemText(1, _translate("InfCalc", "3"))
        self.comboBox_2.setItemText(2, _translate("InfCalc", "4"))
        self.comboBox_2.setItemText(3, _translate("InfCalc", "5"))
        self.comboBox_2.setItemText(4, _translate("InfCalc", "6"))
        self.comboBox_2.setItemText(5, _translate("InfCalc", "7"))
        self.comboBox_2.setItemText(6, _translate("InfCalc", "8"))
        self.comboBox_2.setItemText(7, _translate("InfCalc", "9"))
        self.comboBox_2.setItemText(8, _translate("InfCalc", "10"))
        self.label_2.setText(_translate("InfCalc", "Исходная СС:"))
        self.label_3.setText(_translate("InfCalc", "Конечная СС:"))
        self.pushButton.setText(_translate("InfCalc", "Перевести"))
        self.label_5.setText(_translate("InfCalc", "Подсчет количистово каких либо цифр в числе:"))
        self.label_6.setText(_translate("InfCalc", "Выражение или число:"))
        self.textBrowser.setHtml(_translate("InfCalc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Какую цифру нужно искать</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("InfCalc", "2"))
        self.comboBox_3.setItemText(1, _translate("InfCalc", "3"))
        self.comboBox_3.setItemText(2, _translate("InfCalc", "4"))
        self.comboBox_3.setItemText(3, _translate("InfCalc", "5"))
        self.comboBox_3.setItemText(4, _translate("InfCalc", "6"))
        self.comboBox_3.setItemText(5, _translate("InfCalc", "7"))
        self.comboBox_3.setItemText(6, _translate("InfCalc", "8"))
        self.comboBox_3.setItemText(7, _translate("InfCalc", "9"))
        self.comboBox_3.setItemText(8, _translate("InfCalc", "10"))
        self.comboBox_4.setItemText(0, _translate("InfCalc", "0"))
        self.comboBox_4.setItemText(1, _translate("InfCalc", "1"))
        self.comboBox_4.setItemText(2, _translate("InfCalc", "2"))
        self.comboBox_4.setItemText(3, _translate("InfCalc", "3"))
        self.comboBox_4.setItemText(4, _translate("InfCalc", "4"))
        self.comboBox_4.setItemText(5, _translate("InfCalc", "5"))
        self.comboBox_4.setItemText(6, _translate("InfCalc", "6"))
        self.comboBox_4.setItemText(7, _translate("InfCalc", "7"))
        self.comboBox_4.setItemText(8, _translate("InfCalc", "8"))
        self.comboBox_4.setItemText(9, _translate("InfCalc", "9"))
        self.textBrowser_4.setHtml(_translate("InfCalc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">В какой СС идет подсчет</span></p></body></html>"))
        self.pushButton_2.setText(_translate("InfCalc", "Подсчитать"))
        self.label_7.setText(_translate("InfCalc", "Переводчик из одной единицы памяти в другую :"))
        self.label_8.setText(_translate("InfCalc", "Исходное число:"))
        self.comboBox_5.setItemText(0, _translate("InfCalc", "бит"))
        self.comboBox_5.setItemText(1, _translate("InfCalc", "Кбит"))
        self.comboBox_5.setItemText(2, _translate("InfCalc", "Мбит"))
        self.comboBox_5.setItemText(3, _translate("InfCalc", "Гбит"))
        self.comboBox_5.setItemText(4, _translate("InfCalc", "Тбит"))
        self.comboBox_5.setItemText(5, _translate("InfCalc", "байт"))
        self.comboBox_5.setItemText(6, _translate("InfCalc", "Кбайт"))
        self.comboBox_5.setItemText(7, _translate("InfCalc", "Мбайт"))
        self.comboBox_5.setItemText(8, _translate("InfCalc", "Гбайт"))
        self.comboBox_5.setItemText(9, _translate("InfCalc", "Tбайт"))
        self.label_9.setText(_translate("InfCalc", "Исходная единица:"))
        self.label_10.setText(_translate("InfCalc", "Конечная еденица:"))
        self.comboBox_7.setItemText(0, _translate("InfCalc", "байт"))
        self.comboBox_7.setItemText(1, _translate("InfCalc", "Кбайт"))
        self.comboBox_7.setItemText(2, _translate("InfCalc", "Мбайт"))
        self.comboBox_7.setItemText(3, _translate("InfCalc", "Гбайт"))
        self.comboBox_7.setItemText(4, _translate("InfCalc", "Tбайт"))
        self.comboBox_7.setItemText(5, _translate("InfCalc", "бит"))
        self.comboBox_7.setItemText(6, _translate("InfCalc", "Кбит"))
        self.comboBox_7.setItemText(7, _translate("InfCalc", "Мбит"))
        self.comboBox_7.setItemText(8, _translate("InfCalc", "Гбит"))
        self.comboBox_7.setItemText(9, _translate("InfCalc", "Тбит"))
        self.pushButton_3.setText(_translate("InfCalc", "Перевести"))
        self.textBrowser_6.setHtml(_translate("InfCalc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Справка:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Возведение в стпень знак \'**\'.</span></p></body></html>"))