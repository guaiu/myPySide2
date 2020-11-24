#coding='utf-8'
 
import time
from PySide2 import QtCore, QtGui
 
class LoginHandler(QtCore.QThread):
    finishSignal = QtCore.Signal(list)
    def __init__(self,  parent=None):
        super(LoginHandler,  self).__init__(parent)
        pass
     
    def run(self):
        time.sleep(6)
        self.finishSignal.emit(['hello,','world','!'])