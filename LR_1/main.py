import os
import sys

from cesar import CesarEncoding
from PyQt5 import QtWidgets
import form
import formcreate

inputdir=['C:/User/Default','C:/User/Default','C:/User/Default']
inputfiles=[]
status=CesarEncoding()

class WindowCreate(QtWidgets.QMainWindow, formcreate.Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        self.ButtonChooseDir.clicked.connect(self.browse_dir)
        
        self.ButtonSave.clicked.connect(self.save)
    

    def browse_dir(self):
        inputdir.insert(2, QtWidgets.QFileDialog.getExistingDirectory(self, "Browse"))

    def save(self):
        file=open(inputdir[2]+'/'+self.TextFilename.text(), "w")
        file.write(self.TextContent.toPlainText())
        file.close()
        self.close()

class Window(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        self.ButtonInBrowse.clicked.connect(self.browse_input)
        self.ButtonOutBrowse.clicked.connect(self.browse_output)
        self.ButtonEncrypte.clicked.connect(self.encode)
        self.ButtonDecrypte.clicked.connect(self.decode)
        self.ButtonInCreate.clicked.connect(self.create)
        self.ButtonExit.clicked.connect(self.close)
        self.ButtonAthour.clicked.connect(self.author)
        self.ButtonPrint.clicked.connect(self.print)

    def print(self):
        self.TextTest.clear()
        file=open(inputdir[0]+'/'+self.TextInput.currentItem().text(), encoding="ISO-8859-1")
        res=file.read().splitlines()
        if(res[0]==''):
            res="File: "+self.TextInput.currentItem().text()+" is empty!"
        else:
            for index in res:
                self.TextTest.addItem(index)
        file.close()

    def author(self):
        self.TextTest.clear()
        self.TextTest.addItem("Made in Instrate© by grandmeister Savchuk Bohdan especially for Havrylko Y.V.")

    def create(self):
        self.inst=WindowCreate()
        self.inst.show()
        self.show()

    def browse_input(self):
        self.TextInput.clear()
        directory=QtWidgets.QFileDialog.getExistingDirectory(self, "Browse")
        if directory:
            for file_name in os.listdir(directory):
                self.TextInput.addItem(file_name)
        self.TextInput.setCurrentRow(0)
        inputdir.insert(0, directory)

    def browse_output(self):
        self.TextOutput.clear()
        directory=QtWidgets.QFileDialog.getExistingDirectory(self, "Browse")
        if directory:
            for file_name in os.listdir(directory):
                self.TextOutput.addItem(file_name)
        self.TextOutput.setCurrentRow(0)
        inputdir.insert(1, directory)


    def encode(self, temp):
        self.TextTest.clear()
        status.coding(inputdir[0]+'/'+self.TextInput.currentItem().text(), inputdir[1]+'/'+self.TextOutput.currentItem().text(), int(self.KeyBox.text()), 1)
        res="File: "+self.TextInput.currentItem().text()
        res+="\nhas been encrypted and been writen to"
        res+="\nFile: "+self.TextOutput.currentItem().text()
        self.TextTest.addItem(res)

    def decode(self, temp):
        self.TextTest.clear()
        status.coding(inputdir[0]+'/'+self.TextInput.currentItem().text(), inputdir[1]+'/'+self.TextOutput.currentItem().text(), int(self.KeyBox.text()), -1)
        res="File: "+self.TextInput.currentItem().text()
        res+="\nhas been decrypted and been writen to"
        res+="\nFile: "+self.TextOutput.currentItem().text()
        self.TextTest.addItem(res)


        



def main():
    app=QtWidgets.QApplication(sys.argv)
    window=Window()
    window.show()
    app.exec_()


    


if __name__=='__main__':
    main()