import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 358)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 60, 211, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(300, 60, 211, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "lab1"))
        self.pushButton.setText(_translate("Dialog", "lab2"))
        self.pushButton_5.setText(_translate("Dialog", "lab3"))
        self.pushButton_4.setText(_translate("Dialog", "lab4"))
        self.pushButton_3.setText(_translate("Dialog", "lab5"))
        self.pushButton_6.setText(_translate("Dialog", "lab6"))
        self.pushButton_7.setText(_translate("Dialog", "lab7"))
        self.pushButton_8.setText(_translate("Dialog", "lab8"))
        self.pushButton_9.setText(_translate("Dialog", "lab9"))
        self.pushButton_10.setText(_translate("Dialog", "lab10"))


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_lab2)
        self.pushButton_2.clicked.connect(self.open_lab1)
        self.pushButton_3.clicked.connect(self.open_lab5)
        self.pushButton_4.clicked.connect(self.open_lab4)
        self.pushButton_5.clicked.connect(self.open_lab3)
        self.pushButton_6.clicked.connect(self.open_lab6)
        self.pushButton_7.clicked.connect(self.open_lab7)
        self.pushButton_8.clicked.connect(self.open_lab8)
        self.pushButton_9.clicked.connect(self.open_lab9)
        self.pushButton_10.clicked.connect(self.open_lab10)
    
    @pyqtSlot()
    def open_lab1(self):
        print("Открываем лабораторную работу №1")
        lab = r"C:\Users\PYst\Desktop\labQT_openLab\labQT_1_triatlon\main.py"
        os.startfile(lab)
    
    @pyqtSlot()
    def open_lab2(self):
        print("Открываем лабораторную работу №2")
        lab = r"C:\Users\PYst\Desktop\labQT_openLab\labQT_2_openfail\main.py"
        os.startfile(lab)
    
    @pyqtSlot()
    def open_lab3(self):
        print("Открываем лабораторную работу №3")
        lab = r"C:\Users\PYst\Desktop\labQT_openLab\labQT_3_ExselWord\main.py"
        os.startfile(lab)
    
    @pyqtSlot()
    def open_lab4(self):
        print("Открываем лабораторную работу №4")
        lab = r"C:\Users\PYst\Desktop\labQT_openLab\labQT_4_DataFail\main.py"
        os.startfile(lab)
    
    @pyqtSlot()
    def open_lab5(self):
        print("Открываем лабораторную работу №5")
        lab = r"C:\Users\PYst\Desktop\labQT_openLab\labQT_5_ClockParsing\main.py"
        os.startfile(lab)
    
    @pyqtSlot()
    def open_lab6(self):
        print("Открываем лабораторную работу №6")
        
    
    @pyqtSlot()
    def open_lab7(self):
        print("Открываем лабораторную работу №7")
        
    
    @pyqtSlot()
    def open_lab8(self):
        print("Открываем лабораторную работу №8")
        
    
    @pyqtSlot()
    def open_lab9(self):
        print("Открываем лабораторную работу №9")
        
    
    @pyqtSlot()
    def open_lab10(self):
        print("Открываем лабораторную работу №10")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())