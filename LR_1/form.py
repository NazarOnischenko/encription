# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 5, 1, 1)
        self.TextInput = QtWidgets.QListWidget(self.centralwidget)
        self.TextInput.setObjectName("TextInput")
        self.gridLayout.addWidget(self.TextInput, 1, 0, 4, 2)
        self.ButtonEncrypte = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonEncrypte.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonEncrypte.setObjectName("ButtonEncrypte")
        self.gridLayout.addWidget(self.ButtonEncrypte, 1, 2, 1, 1)
        self.TextOutput = QtWidgets.QListWidget(self.centralwidget)
        self.TextOutput.setObjectName("TextOutput")
        self.gridLayout.addWidget(self.TextOutput, 1, 3, 4, 3)
        self.ButtonDecrypte = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDecrypte.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonDecrypte.setObjectName("ButtonDecrypte")
        self.gridLayout.addWidget(self.ButtonDecrypte, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.KeyBox = QtWidgets.QSpinBox(self.centralwidget)
        self.KeyBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.KeyBox.setMinimum(-9999999)
        self.KeyBox.setMaximum(9999999)
        self.KeyBox.setProperty("value", 1)
        self.KeyBox.setDisplayIntegerBase(10)
        self.KeyBox.setObjectName("KeyBox")
        self.gridLayout.addWidget(self.KeyBox, 4, 2, 1, 1)
        self.ButtonInBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonInBrowse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonInBrowse.setObjectName("ButtonInBrowse")
        self.gridLayout.addWidget(self.ButtonInBrowse, 5, 0, 1, 1)
        self.ButtonInCreate = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonInCreate.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.ButtonInCreate.setObjectName("ButtonInCreate")
        self.gridLayout.addWidget(self.ButtonInCreate, 5, 1, 1, 1)
        self.ButtonPrint = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonPrint.setObjectName("ButtonPrint")
        self.gridLayout.addWidget(self.ButtonPrint, 5, 2, 1, 1)
        self.ButtonOutBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonOutBrowse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonOutBrowse.setObjectName("ButtonOutBrowse")
        self.gridLayout.addWidget(self.ButtonOutBrowse, 5, 3, 1, 1)
        self.ButtonExit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ButtonExit.setFont(font)
        self.ButtonExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonExit.setObjectName("ButtonExit")
        self.gridLayout.addWidget(self.ButtonExit, 5, 4, 1, 1)
        self.ButtonAthour = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ButtonAthour.setFont(font)
        self.ButtonAthour.setObjectName("ButtonAthour")
        self.gridLayout.addWidget(self.ButtonAthour, 5, 5, 1, 1)
        self.TextTest = QtWidgets.QListWidget(self.centralwidget)
        self.TextTest.setObjectName("TextTest")
        self.gridLayout.addWidget(self.TextTest, 6, 0, 1, 6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab module #1"))
        self.label.setText(_translate("MainWindow", "Input file"))
        self.label_2.setText(_translate("MainWindow", "Output file"))
        self.ButtonEncrypte.setText(_translate("MainWindow", "Encrypte"))
        self.ButtonDecrypte.setText(_translate("MainWindow", "Decrypte"))
        self.label_3.setText(_translate("MainWindow", "Key"))
        self.ButtonInBrowse.setText(_translate("MainWindow", "Browse"))
        self.ButtonInCreate.setText(_translate("MainWindow", "Create"))
        self.ButtonPrint.setText(_translate("MainWindow", "Print"))
        self.ButtonOutBrowse.setText(_translate("MainWindow", "Browse"))
        self.ButtonExit.setText(_translate("MainWindow", "EXIT"))
        self.ButtonAthour.setText(_translate("MainWindow", "Author"))
