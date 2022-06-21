import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
import pa
from passsave import *
from mainlog import loginon


class Passwardsolve(QtWidgets.QMainWindow, pa.Ui_PDSE):
    def __init__(self, parent = None):
        super(Passwardsolve, self).__init__()
        self.setupUi(self)
        self.setStyleSheet("#PDSE{border-image:url(maomi.jpg)}")
        self.show()
    def pk1(self):
        Web = self.lineEdit.text()
        User = self.lineEdit_2.text()
        passward = self.lineEdit_3.text()
        pamakes = self.lineEdit_4.text()
        passsave(Web, User, passward, pamakes)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
    def pk2(self):
        Web = self.lineEdit.text()
        User = self.lineEdit_2.text()
        passward = self.lineEdit_3.text()
        pamakes = self.lineEdit_4.text()
        passchange(Web, User, passward, pamakes)
    def pk3(self):
        tex = self.lineEdit_5.text()
        if tex == '':
            self.textBrowser.clear()
            return
        ff = open(f"./Psave/{tex}.txt", 'r')
        ffr = ff.read()
        print(ffr)
        ff.close()
        self.textBrowser.append(ffr)
    def pk4(self):
        file = items()
        for i in file:
            b = str(i).rstrip('.txt')
            self.textBrowser_2.append(b)
    def pk5(self):
        self.textBrowser_2.clear()


App = QtWidgets.QApplication(sys.argv)
logindiag = loginon()
ret = logindiag.exec()
if ret == QDialog.Accepted:
    mywind = Passwardsolve()
sys.exit(App.exec_())






