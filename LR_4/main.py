import os
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
import rsa
import form
#import soloKeys

class Window(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ButtonBrowse.clicked.connect(self.methodBrowse)
        self.ButtonImportKey.clicked.connect(self.methodImportKeys)
        self.ButtonEncrypte.clicked.connect(self.methodEncrypt)
        self.ButtonDecrypte.clicked.connect(self.methodDecrypte)

    def methodBrowse(self):
        self.TextBrowser.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Browse")
        if directory:
            for file_name in os.listdir(directory):
                if(file_name.endswith('.pem')==False):
                    self.TextBrowser.addItem(file_name)
        self.TextBrowser.setCurrentRow(0)
        self.inputdir=[directory]

    def methodImportKeys(self):
        self.TextPublicKey.clear()
        self.TextPrivateKey.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Browse keys")
        if directory:
            for file_name in os.listdir(directory):
                if(file_name.endswith('.pem')==True):
                    self.TextPublicKey.addItem(file_name)
                    self.TextPrivateKey.addItem(file_name)
        self.TextPublicKey.setCurrentRow(0)
        self.TextPrivateKey.setCurrentRow(0)
        if(len(self.inputdir)==1):
            self.inputdir.append(directory)
        else:
            self.inputdir[1]=directory

    def methodEncrypt(self):
        self.TextOutput.clear()
        if(hasattr(self, 'key_public') == False):
            self.key_public = importKey(self.inputdir[1]+'/'+self.TextPublicKey.currentItem().text(),True)
            #self.key_private = importKey(self.inputdir[1]+'/'+self.TextPrivateKey.currentItem().text(),False)
        file = open(self.inputdir[0]+'/'+self.TextBrowser.currentItem().text())
        text = file.read()
        file.close()
        text = encrypt(text, self.key_public)
        file = open(self.inputdir[0]+'/'+self.TextBrowser.currentItem().text()+'RSA-encr.bin','wb')
        file.write(text)
        file.close()
        self.TextOutput.addItem('File has been encrypted')

    def methodDecrypte(self):
        self.TextOutput.clear()
        if(hasattr(self, 'key_private') == False):
            self.key_private = importKey(self.inputdir[1]+'/'+self.TextPrivateKey.currentItem().text(),False)
        file = open(self.inputdir[0]+'/'+self.TextBrowser.currentItem().text(),'rb')
        text = file.read()
        file.close()
        text = decrypt(text, self.key_private)
        file = open(self.inputdir[0]+'/'+self.TextBrowser.currentItem().text()+'RSA-decr.txt','w')
        file.write(str(text.decode('utf-8')))
        file.close()
        self.TextOutput.addItem('File has been decrypted')

class NotCompatible(Exception):
    def __init__(self, text):
        self.text = text

def generateKeys(size):
    try:
        if(size % 8 != 0 ):
            raise NotCompatible("It's not a compatible for the key")
    except NotCompatible as BadSize:
        print(BadSize)
    finally:
        pub, priv = rsa.newkeys(size)
        exportKey('PublicKey',pub.save_pkcs1())
        exportKey('PrivateKey', priv.save_pkcs1())

def exportKey(filename, key):
    file = open(filename+'.pem', 'wb')
    file.write(key)
    file.close()

def importKey(filename, isPublicKey):
    file = open(filename, 'rb')
    key_temp = file.read()
    if(isPublicKey == True):
        return rsa.PublicKey.load_pkcs1(key_temp, format='PEM')
    return rsa.PrivateKey.load_pkcs1(key_temp, format='PEM')

def encrypt(text, key_public):
    result = text.encode('utf-8')
    result = rsa.encrypt(result, key_public)
    return result

def decrypt(text, key_private):
    return rsa.decrypt(text, key_private)

def main():
    # generateKeys(1024)
    
    # key_public = importKey('PublicKey.pem', False)
    # key_private = importKey('PrivateKey.pem',True)
    
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

    return 0

if (__name__=="__main__"):
    main()
