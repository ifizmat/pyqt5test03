# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 500)
        self.test_label = QtWidgets.QLabel(Dialog)
        self.test_label.setGeometry(QtCore.QRect(50, 50, 800, 200))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.test_label.setFont(font)
        self.test_label.setObjectName("test_label")
        self.start_button = QtWidgets.QPushButton(Dialog)
        self.start_button.setGeometry(QtCore.QRect(50, 300, 150, 70))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(32)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(Dialog)
        self.stop_button.setGeometry(QtCore.QRect(250, 300, 150, 70))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(32)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName("stop_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Test PyQt5 QDialog v0.2"))
        self.test_label.setText(_translate("Dialog", "Test PyQt5 QLabel."))
        self.start_button.setText(_translate("Dialog", "Start"))
        self.stop_button.setText(_translate("Dialog", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
