# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reproduce.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DecFuzzer(object):
    def setupUi(self, DecFuzzer):
        DecFuzzer.setObjectName("DecFuzzer")
        DecFuzzer.resize(405, 312)
        self.label = QtWidgets.QLabel(DecFuzzer)
        self.label.setGeometry(QtCore.QRect(10, 0, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(DecFuzzer)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 251, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox = QtWidgets.QComboBox(DecFuzzer)
        self.comboBox.setGeometry(QtCore.QRect(270, 30, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(DecFuzzer)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DecFuzzer)
        self.label_3.setGeometry(QtCore.QRect(270, 60, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(DecFuzzer)
        self.lineEdit.setGeometry(QtCore.QRect(270, 80, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(DecFuzzer)
        self.label_4.setGeometry(QtCore.QRect(270, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(DecFuzzer)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 120, 81, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(DecFuzzer)
        self.pushButton.setGeometry(QtCore.QRect(360, 120, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(DecFuzzer)
        self.label_5.setGeometry(QtCore.QRect(270, 150, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(DecFuzzer)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 170, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(DecFuzzer)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 170, 81, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(DecFuzzer)
        self.checkBox.setGeometry(QtCore.QRect(270, 200, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.layoutWidget = QtWidgets.QWidget(DecFuzzer)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 222, 124, 83))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(DecFuzzer)
        QtCore.QMetaObject.connectSlotsByName(DecFuzzer)

    def retranslateUi(self, DecFuzzer):
        _translate = QtCore.QCoreApplication.translate
        DecFuzzer.setWindowTitle(_translate("DecFuzzer", "Form"))
        self.label.setText(_translate("DecFuzzer", "reproduce.py"))
        self.comboBox.setItemText(0, _translate("DecFuzzer", "r2"))
        self.comboBox.setItemText(1, _translate("DecFuzzer", "retdec"))
        self.comboBox.setItemText(2, _translate("DecFuzzer", "Jeb"))
        self.comboBox.setItemText(3, _translate("DecFuzzer", "IDA"))
        self.comboBox.setItemText(4, _translate("DecFuzzer", "Other"))
        self.label_2.setText(_translate("DecFuzzer", "Decompilers:"))
        self.label_3.setText(_translate("DecFuzzer", "<html><head/><body><p>Other Decompilers:</p></body></html>"))
        self.label_4.setText(_translate("DecFuzzer", "files_dir:"))
        self.pushButton.setText(_translate("DecFuzzer", "..."))
        self.label_5.setText(_translate("DecFuzzer", "emi_dir:"))
        self.pushButton_2.setText(_translate("DecFuzzer", "..."))
        self.checkBox.setText(_translate("DecFuzzer", "--EMI"))
        self.pushButton_5.setText(_translate("DecFuzzer", "Run the process"))
        self.pushButton_4.setText(_translate("DecFuzzer", "Stop the process"))
        self.pushButton_3.setText(_translate("DecFuzzer", "Return to main menu"))
