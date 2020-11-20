#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo2 通过pyside2-rcc转换.ui文件为.py文件后载入
# 命令行：pyside2-uic mainwindow.ui > ui_mainwindow.py

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())