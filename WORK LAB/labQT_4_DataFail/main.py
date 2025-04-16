import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets

# Функция для загрузки и обработки JSON-данных
def load_json_data():
        with open('exer1-interface-data.json', 'r') as file:
            jsondata = file.read()
            return json.loads(jsondata)

# Класс UI для основного окна приложения
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(620, 30, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_getData = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_getData.setObjectName("pushButton_getData")
        self.verticalLayout.addWidget(self.pushButton_getData)
        self.pushButton_clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout.addWidget(self.pushButton_clear)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 571, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Интерфейс управления"))
        self.pushButton_getData.setText(_translate("MainWindow", "Получить данные"))
        self.pushButton_clear.setText(_translate("MainWindow", "Очистить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DN"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "AdminSt"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Speed"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MTU"))

# Основной класс приложения
class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_getData.clicked.connect(self.get_data_from_json)
        self.pushButton_clear.clicked.connect(self.clear_table)

    # Метод для получения данных из JSON-файла и заполнения таблицы
    def get_data_from_json(self):
        json_data = load_json_data()
        if json_data is not None:
            self.fill_table_with_data(json_data)
    
    # Метод для очистки таблицы
    def clear_table(self):
        self.tableWidget.setRowCount(0)

    # Метод для заполнения таблицы данными
    def fill_table_with_data(self, data):
        self.tableWidget.setRowCount(0)
        for index, entry in enumerate(data['imdata']):
            self.tableWidget.insertRow(index)
            dn = entry['l1PhysIf']['attributes']['dn']
            adminSt = entry['l1PhysIf']['attributes']['adminSt']
            speed = entry['l1PhysIf']['attributes']['speed']
            mtu = entry['l1PhysIf']['attributes']['mtu']
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(str(dn)))
            self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(adminSt))
            self.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(speed))
            self.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(mtu))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())