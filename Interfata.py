# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfata.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 200, 561, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 130, 561, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.SelecteazaTabelul = QtWidgets.QComboBox(self.groupBox_3)
        self.SelecteazaTabelul.setGeometry(QtCore.QRect(20, 20, 421, 22))
        self.SelecteazaTabelul.setObjectName("SelecteazaTabelul")
        self.SelecteazaTab = QtWidgets.QPushButton(self.groupBox_3)
        self.SelecteazaTab.setGeometry(QtCore.QRect(450, 20, 91, 23))
        self.SelecteazaTab.setObjectName("SelecteazaTab")
        self.AfiseazaChei = QtWidgets.QPushButton(self.centralwidget)
        self.AfiseazaChei.setGeometry(QtCore.QRect(240, 370, 171, 41))
        self.AfiseazaChei.setObjectName("AfiseazaChei")
        self.Iesire = QtWidgets.QPushButton(self.centralwidget)
        self.Iesire.setGeometry(QtCore.QRect(460, 560, 181, 41))
        self.Iesire.setObjectName("Iesire")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 561, 80))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(300, 20, 61, 16))
        self.label_3.setObjectName("label_3")
        self.ButonConectare = QtWidgets.QPushButton(self.groupBox)
        self.ButonConectare.setGeometry(QtCore.QRect(200, 50, 91, 23))
        self.ButonConectare.setObjectName("ButonConectare")
        self.User = QtWidgets.QLineEdit(self.groupBox)
        self.User.setGeometry(QtCore.QRect(50, 20, 113, 20))
        self.User.setObjectName("User")
        self.Parola = QtWidgets.QLineEdit(self.groupBox)
        self.Parola.setGeometry(QtCore.QRect(360, 20, 131, 20))
        self.Parola.setObjectName("Parola")
        self.adauga = QtWidgets.QPushButton(self.centralwidget)
        self.adauga.setGeometry(QtCore.QRect(30, 560, 191, 41))
        self.adauga.setObjectName("adauga")
        self.numeColoane = QtWidgets.QTableWidget(self.centralwidget)
        self.numeColoane.setGeometry(QtCore.QRect(250, 490, 181, 111))
        self.numeColoane.setColumnCount(1)
        self.numeColoane.setObjectName("numeColoane")
        self.numeColoane.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 420, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 420, 201, 16))
        self.label_4.setObjectName("label_4")
        self.CheiePrimara = QtWidgets.QComboBox(self.centralwidget)
        self.CheiePrimara.setGeometry(QtCore.QRect(40, 450, 181, 22))
        self.CheiePrimara.setObjectName("CheiePrimara")
        self.faraConstrangere = QtWidgets.QComboBox(self.centralwidget)
        self.faraConstrangere.setGeometry(QtCore.QRect(450, 450, 171, 22))
        self.faraConstrangere.setObjectName("faraConstrangere")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 420, 161, 16))
        self.label_5.setObjectName("label_5")
        self.tabel = QtWidgets.QComboBox(self.centralwidget)
        self.tabel.setGeometry(QtCore.QRect(250, 450, 181, 22))
        self.tabel.setObjectName("tabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Selecteaza tabelul"))
        self.SelecteazaTab.setText(_translate("MainWindow", "Selecteaza"))
        self.AfiseazaChei.setText(_translate("MainWindow", "Afiseaza cheile"))
        self.Iesire.setText(_translate("MainWindow", "Iesire"))
        self.groupBox.setTitle(_translate("MainWindow", "Conexiune"))
        self.label.setText(_translate("MainWindow", "User"))
        self.label_3.setText(_translate("MainWindow", "Parola"))
        self.ButonConectare.setText(_translate("MainWindow", "Conectare"))
        self.adauga.setText(_translate("MainWindow", "Adauga constrangere"))
        self.label_2.setText(_translate("MainWindow", "Coloane din tabelul curent"))
        self.label_4.setText(_translate("MainWindow", "Tabel in care se va adauga constrangerea"))
        self.label_5.setText(_translate("MainWindow", "Se poate adauga pe:"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
