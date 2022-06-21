import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import login


class loginon(QDialog, login.Ui_Dialog):
    UD = '1'
    PD = '1'
    def __init__(self,parent =None):
        super(loginon, self).__init__()
        self.setupUi(self)
        self.setStyleSheet("#Dialog{border-image:url(likepink.jpeg)}")
        self.show()
    def clickcon(self):
        Userdata = self.lineEdit.text()
        PassWarad = self.lineEdit_2.text()
        if Userdata == self.UD and PassWarad == self.PD:
            self.accept()
        else:
            qWarning('passward or Admain not right!')
