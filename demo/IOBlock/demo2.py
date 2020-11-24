#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo2 使用多线程、使按钮暂时失效 解决卡顿问题
# 分析：多线程=其他线程有机会执行，按钮暂时失效=使用同步方案
# 这里主要体现的还是同步方案，多线程的使用在这里形同虚设（这个例子有时间再进行拆分）
# 所以这里主线程该阻塞还是阻塞了，顶多不会卡到闪退

 
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
        #time.sleep(6)
        #print("hello, world")
        #self.pushButton_login.setDisabled(False)
         
        #采用多线程操作
        from LoginHandler import LoginHandler
        self.login_process = LoginHandler()
        #登陆完成的信号绑定到登陆结束的槽函数
        self.login_process.finishSignal.connect(self.LoginEnd)
        #启动线程
        self.login_process.start()
        pass
     
         
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())