import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *# Это наш конвертированный файл дизайна
import form
from random import randint
class Window(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Apply.clicked.connect(self.methodApply)
        self.Exit.clicked.connect(self.methodClose)
    #получаем имена файлов
    filename = 'key.txt'
    #filenameInit = 'text.txt'
    #filenameOut = 'result.txt'
    def methodApply(self):
        if self.ComboBox.currentIndex()==0:
            self.cript()
        elif self.ComboBox.currentIndex()==1:
            self.decript()
    def methodClose(self):
        self.close()
    result = dict()
    arr = []
    temp = []
    string = []
    list_result = []
    list_resultDecript = []
    def cript(self):
        #открываем файл для получения ключа кодировки
        file = open(self.filename,encoding='utf-8')
        #получаем список букв размером 10х10
        for i in range(10):
            self.arr.append(file.read(10))
            self.temp.append(file.readline())
        #закрываем файл
        file.close()
        text = self.Input.toPlainText()
        text = text.lower()
        #проверяем каждую букву со списком 
        #если есть буква в списке возвращаем ее индексы i/j 
        #так как спискы начинаються с нуля,а нам нужно начинать список с единицы мы возвращаем i+1/j+1
        for k in text:
            self.result[k] = ''
            for i in range(len(self.arr)):
                for j in range(len(self.arr)):
                    if k==self.arr[i][j]:
                        self.result[k]+=str(i+1)+'/'+str(j+1)+' '
        #вытягиваем значения из словаря в список
        #и генерируем рандомным образом шифр
        for k in text:
            i = 0
            for key in self.result:
                if self.result[key]!='':
                    self.string.append(self.result[key].split(' '))
                else:
                    self.string.append(['-'])
                if '' in self.string[i]:
                    self.string[i].remove('') 
                if key == k:
                    rand = randint(0,len(self.string[i])-1)
                    self.list_result.append(self.string[i][rand])
                i += 1
        #выводим массив стиха в таблицу
        for i in range(len(self.arr)):
            for j in range(len(self.arr)):    
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(self.arr[i][j])))
        #выводим шифр
        self.Output.append(' '.join(self.list_result))

    def decript(self):
        text = self.Input.toPlainText()
        text_list = []
        text_list = text.split(' ')
        indI = 0
        indJ = 0
        for k in text_list:
            if k != '-':
                if len(k) == 4 and k[2]=='/':
                    indI = int(str(k[0])+str(k[1]))-1
                    indJ = int(k[3])-1
                elif len(k) == 4 and k[1]=='/':
                    indI = int(k[0])-1
                    indJ = int(str(k[2])+str(k[3]))-1
                else:
                    indI = int(k[0])-1
                    indJ = int(k[2])-1
                for i in range(len(self.arr)):
                    for j in range(len(self.arr)):
                        if indI == i and indJ == j:
                            self.list_resultDecript.append(self.arr[i][j])
            else:
                self.list_resultDecript.append('-')
        for i in range(len(self.arr)):
            for j in range(len(self.arr)):    
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(self.arr[i][j])))
        self.Output.clear()
        self.Output.append(''.join(self.list_resultDecript))
        
                
def main():
    app=QtWidgets.QApplication(sys.argv)
    window=Window()
    window.show()
    app.exec_()

    


if __name__=='__main__':
    main()