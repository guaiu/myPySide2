#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo1 有阻塞的程序
# 十分卡顿，疯狂点击按钮还会闪退

 
"""
Module implementing MainWindow.
"""
 
import time

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2 import QtCore,  QtGui
 
from Ui_main import Ui_MainWindow
 
 
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        
        Constructor 
        @param parent reference to the parent widget
        @type QWidget
        
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
     
    @Slot(list)
    def LoginEnd(self, words):
        for i in words:
            print(i)
        self.pushButton_login.setDisabled(False)
        pass
        
    @Slot()
    def on_pushButton_login_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.pushButton_login.setDisabled(True)
        #采用单线程操作
        time.sleep(6)
        print("hello, world")
        self.pushButton_login.setDisabled(False)
     
         
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())