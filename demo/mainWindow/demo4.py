#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo4 .ui转化的.py文件的两种使用方式

import sys

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QWidget

from ui_calc import Ui_Calc

# 方式一：实例化方式
class MyCalc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Calc()
        self.ui.setupUi(self)

    @Slot(int)
    def on_inputSpinBox1_valueChanged(self, value):
        self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox2.value()))

    @Slot(int)
    def on_inputSpinBox2_valueChanged(self, value):
        self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox1.value()))
		
		
# 方式二：使用多继承的方式
class MyCalc2(QWidget, Ui_Calc):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    @Slot(int)
    def on_inputSpinBox1_valueChanged(self, value):
        self.outputWidget.setText(str(value + self.inputSpinBox2.value()))

    @Slot(int)
    def on_inputSpinBox2_valueChanged(self, value):
        self.outputWidget.setText(str(value + self.inputSpinBox1.value()))
		
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyCalc()
    # win = MyCalc2()
    win.show()
    sys.exit(app.exec_())