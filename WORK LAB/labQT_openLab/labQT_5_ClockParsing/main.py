from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests
from bs4 import BeautifulSoup

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 451, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Номер', 'Название', 'Время'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setRowCount(0)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 20, 111, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Data = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Data.setObjectName("Data")
        self.verticalLayout.addWidget(self.Data)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Data.setText(_translate("MainWindow", "Получить данные"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить"))

class NewsParserApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(NewsParserApp, self).__init__()
        self.setupUi(self)
        self.Data.clicked.connect(self.fetch_and_display_news)
        self.pushButton_2.clicked.connect(self.clear_table)

    def fetch_and_display_news(self):
        news_items = get_news_data()
        self.populate_table(news_items)

    def populate_table(self, news_items):
        self.tableWidget.setRowCount(len(news_items))
        for row, item in enumerate(news_items):
            number_item = QtWidgets.QTableWidgetItem(str(row + 1))
            title_item = QtWidgets.QTableWidgetItem(item['title'])
            time_item = QtWidgets.QTableWidgetItem(item['time'])

            if item['is_main']:
                color = QtGui.QColor(255, 0, 0)  # Для главных новостей
            else:
                color = QtGui.QColor(0, 128, 0)  # Для второстепенных новостей

            number_item.setBackground(color)
            title_item.setBackground(color)
            time_item.setBackground(color)

            self.tableWidget.setItem(row, 0, number_item)
            self.tableWidget.setItem(row, 1, title_item)
            self.tableWidget.setItem(row, 2, time_item)

    def clear_table(self):
        self.tableWidget.setRowCount(0)

def get_news_data():
    url = 'https://ria.ru/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_items = []

    # Получение главных новостей
    main_news_titles = soup.select('.cell-main-photo__title')
    main_news_times = soup.select('.cell-main-photo__info')

    for title, time in zip(main_news_titles, main_news_times):
        news_item = {
            'title': title.text.strip(),
            'time': time.text.strip(),
            'is_main': True
        }
        news_items.append(news_item)

    # Получение второстепенных новостей
    secondary_news_titles = soup.select('.cell-list__item-title')
    secondary_news_times = soup.select('.cell-list__item-info')

    for title, time in zip(secondary_news_titles, secondary_news_times):
        news_item = {
            'title': title.text.strip(),
            'time': time.text.strip(),
            'is_main': False
        }
        news_items.append(news_item)

    return news_items

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = NewsParserApp()
    window.show()
    sys.exit(app.exec_())