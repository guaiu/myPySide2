#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo3 使用ui代码实现界面和逻辑的源代码分离

import sys
from PySide2.QtWidgets import QApplication,QMainWindow,QFileDialog
import mainUi
class MainCode(QMainWindow,mainUi.Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		mainUi.Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.btn_save.clicked.connect(self.on_save)
		self.btn_open.clicked.connect(self.on_open)
 
	def on_save(self):
		FullFileName,_=QFileDialog.getSaveFileName (self, '文件另存为', r'./','TXT (*.txt)')
		set_text=self.txt_view.toPlainText()
		with open(FullFileName,'wt') as f:
			print(set_text, file = f)
 
	def on_open(self):
		txtstr=""
		FullFileName, _ = QFileDialog.getOpenFileName(self, '打开', r'./', 'TXT (*.txt)')
		with open(FullFileName, 'rt') as f:
			lines=f.readlines()
			for line in lines:
				txtstr=txtstr+line
		self.txt_view.setText(txtstr)
 
 
if __name__=='__main__':
	app=QApplication(sys.argv)
	md=MainCode()
	md.show()
	sys.exit(app.exec_())