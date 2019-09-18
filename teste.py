import sys
from PyQt5 import QtWidgets
import Interfata
import cx_Oracle

exclude=" table_name != 'APEX$_ACL' and table_name != 'APEX$_WS_FILES' and table_name != 'APEX$_WS_FILES' and table_name != 'APEX$_WS_HISTORY' and table_name != 'APEX$_WS_LINKS' and table_name != 'APEX$_WS_NOTES' and table_name != 'APEX$_WS_ROWS' and table_name != 'APEX$_WS_TAGS' and table_name != 'APEX$_WS_WEBPG_SECTIONS' and table_name != 'APEX$_WS_WEBPG_SECTION_HISTORY'"
exclude1=" and table_name != 'DEMO_CUSTOMERS' and table_name != 'DEMO_ORDERS' and table_name != 'DEMO_ORDER_ITEMS' and table_name != 'DEMO_PRODUCT_INFO' and table_name != 'DEMO_STATES' and table_name != 'DEMO_USERS' and table_name != 'HTMLDB_PLAN_TABLE'"

class MyQtApp(Interfata.Ui_MainWindow,QtWidgets.QMainWindow):


    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.ButonConectare.clicked.connect(self.conexiune)
        self.SelecteazaTab.clicked.connect(self.afisare)
        self.AfiseazaChei.clicked.connect(self.chei)
        self.adauga.clicked.connect(self.constrangere)
        self.Iesire.clicked.connect(self.iesire)

    def conexiune(self):
        dsn_tns=cx_Oracle.makedsn('DESKTOP-BDF67G7', '1521', service_name='XE')
        conn = cx_Oracle.connect(user=self.User.text(), password=self.Parola.text(), dsn=dsn_tns)
        mycursor = conn.cursor()
        self.SelecteazaTabelul.clear()
        query="select table_name from user_tables where" + exclude+exclude1
        mycursor.execute(query)
        for i in mycursor:
            self.SelecteazaTabelul.addItems(i)
            
    
    def afisare(self):
        dsn_tns=cx_Oracle.makedsn('DESKTOP-BDF67G7', '1521', service_name='XE')
        conn = cx_Oracle.connect(user=self.User.text(), password=self.Parola.text(), dsn=dsn_tns)
        mycursor=conn.cursor()
        self.tableWidget.clear()
        bd=self.SelecteazaTabelul.currentText()
        query="SELECT * FROM "+bd
        result=mycursor.execute(query)
        self.tableWidget.setRowCount(0)      
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                
    def chei(self):
        dsn_tns=cx_Oracle.makedsn('DESKTOP-BDF67G7', '1521', service_name='XE')
        conn = cx_Oracle.connect(user=self.User.text(), password=self.Parola.text(), dsn=dsn_tns)
        mycursor = conn.cursor()
        self.numeColoane.clear()
        ceva=" and table_name != '"+self.SelecteazaTabelul.currentText()+"'"
        query1="select table_name from user_tables where"+exclude+exclude1+ceva
        mycursor.execute(query1)
        for i in mycursor:
            self.CheieStraina.addItems(i)
        ceva3="'"+self.CheieStraina.currentText()+"'"
        query3="SELECT cols.column_name FROM all_constraints cons, all_cons_columns cols WHERE cons.constraint_type != 'P' AND cons.constraint_type != 'FK' AND cons.constraint_name = cols.constraint_name AND cols.table_name="+ceva3
        adaugaTabel=mycursor.execute(query3)
        self.faraConstrangere.clear()
        for i in adaugaTabel:
            self.faraConstrangere.addItems(i)       
        ceva1=" and table_name = '"+self.CheieStraina.currentText()+"'"
        query="SELECT COLUMN_NAME FROM ALL_COL_COMMENTS WHERE"+exclude+exclude1+ceva1
        result=mycursor.execute(query)
        self.numeColoane.setRowCount(0)      
        for row_number,row_data in enumerate(result):
            self.numeColoane.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.numeColoane.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        bd="'"+self.SelecteazaTabelul.currentText()+"'"
        self.CheiePrimara.clear()
        query2="SELECT cols.column_name FROM all_constraints cons, all_cons_columns cols WHERE cons.constraint_type != 'P' AND cons.constraint_name = cols.constraint_name AND cols.table_name="+bd

        mycursor.execute(query2)
        for i in mycursor:
            self.CheiePrimara.addItems(i)
        
    def constrangere(self):
        dsn_tns=cx_Oracle.makedsn('DESKTOP-BDF67G7', '1521', service_name='XE')
        conn = cx_Oracle.connect(user=self.User.text(), password=self.Parola.text(), dsn=dsn_tns)
        mycursor = conn.cursor()
        query="ALTER TABLE "+self.SelecteazaTabelul.currentText()+" ADD CONSTRAINT fk_"+self.CheiePrimara.currentText()+"_"+self.faraConstrangere.currentText()+" FOREIGN KEY ("+self.CheiePrimara.currentText()+") REFERENCES "+self.CheieStraina.currentText()+"("+self.faraConstrangere.currentText()+")"
        mycursor.execute(query)
        
        self.CheieStraina.clear()
        self.CheiePrimara.clear()
        self.numeColoane.clear()
        self.faraConstrangere.clear()

    def iesire(self):
        MyQtApp().destroy()
        
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    qt_app=MyQtApp()
    qt_app.show()
    app.exec_()
