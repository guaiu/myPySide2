# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'E:\demo_project\pyqt_demo\main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
 
from PySide2 import QtCore, QtWidgets
 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
 
try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(475, 264)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton_login = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_login.setGeometry(QtCore.QRect(102, 66, 257, 95))
        self.pushButton_login.setStyleSheet(_fromUtf8("font: 18pt \"Adobe Devanagari\";"))
        self.pushButton_login.setObjectName(_fromUtf8("pushButton_login"))
        MainWindow.setCentralWidget(self.centralWidget)
 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_login.setText(_translate("MainWindow", "点击我登陆", None))
 
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())