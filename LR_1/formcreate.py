# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.TextFilename = QtWidgets.QLineEdit(self.centralwidget)
        self.TextFilename.setObjectName("TextFilename")
        self.gridLayout.addWidget(self.TextFilename, 1, 0, 1, 2)
        self.ButtonChooseDir = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonChooseDir.setObjectName("ButtonChooseDir")
        self.gridLayout.addWidget(self.ButtonChooseDir, 2, 0, 1, 1)
        self.ButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSave.setObjectName("ButtonSave")
        self.gridLayout.addWidget(self.ButtonSave, 2, 1, 1, 1)
        self.TextContent = QtWidgets.QTextEdit(self.centralwidget)
        self.TextContent.setObjectName("TextContent")
        self.gridLayout.addWidget(self.TextContent, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Create File"))
        self.TextFilename.setText(_translate("MainWindow", "Filename.txt"))
        self.ButtonChooseDir.setText(_translate("MainWindow", "Choose directory"))
        self.ButtonSave.setText(_translate("MainWindow", "Save"))
