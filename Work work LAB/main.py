import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(669, 340)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 50, 181, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(280, 170, 55, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 80, 431, 157))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 3, 2, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 4, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 5, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 5, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 4, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 4, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(190, 260, 251, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_2.addWidget(self.lineEdit_13, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Соревнование по триатлону"))
        self.label_6.setText(_translate("Dialog", "Максим"))
        self.label_4.setText(_translate("Dialog", "Андрей"))
        self.label_10.setText(_translate("Dialog", "Общее время (мин)"))
        self.label_7.setText(_translate("Dialog", "Плаванье (м/мин)"))
        self.label_9.setText(_translate("Dialog", "Бег (км/час)"))
        self.label_8.setText(_translate("Dialog", "Велосипед (км/час)"))
        self.label_2.setText(_translate("Dialog", "Скорость"))
        self.label_5.setText(_translate("Dialog", "Егор"))
        self.pushButton.setText(_translate("Dialog", "Время"))
        self.pushButton_2.setText(_translate("Dialog", "Чемпион"))

class TriathlonApp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Привязка кнопок к методам
        self.pushButton.clicked.connect(self.calculate_total_time)
        self.pushButton_2.clicked.connect(self.find_champion)

    def calculate_total_time(self):
        # Константы для дистанций
        SWIM_DISTANCE = 1500  # метров
        BIKE_DISTANCE = 40  # километров
        RUN_DISTANCE = 10  # километров

        try:
            # Андрей
            swim_speed_andrey = float(self.lineEdit.text() or 0)
            bike_speed_andrey = float(self.lineEdit_4.text() or 0)
            run_speed_andrey = float(self.lineEdit_7.text() or 0)
            total_time_andrey = (
                self.calculate_time(swim_speed_andrey, SWIM_DISTANCE / 60) +  # Перевод в минуты
                self.calculate_time(bike_speed_andrey, BIKE_DISTANCE) * 60 +  # Перевод в минуты
                self.calculate_time(run_speed_andrey, RUN_DISTANCE) * 60      # Перевод в минуты
            )
            self.lineEdit_10.setText(f"{total_time_andrey:.2f}")

            # Егор
            swim_speed_egor = float(self.lineEdit_2.text() or 0)
            bike_speed_egor = float(self.lineEdit_5.text() or 0)
            run_speed_egor = float(self.lineEdit_8.text() or 0)
            total_time_egor = (
                self.calculate_time(swim_speed_egor, SWIM_DISTANCE / 60) +
                self.calculate_time(bike_speed_egor, BIKE_DISTANCE) * 60 +
                self.calculate_time(run_speed_egor, RUN_DISTANCE) * 60
            )
            self.lineEdit_11.setText(f"{total_time_egor:.2f}")

            # Максим
            swim_speed_maxim = float(self.lineEdit_3.text() or 0)
            bike_speed_maxim = float(self.lineEdit_6.text() or 0)
            run_speed_maxim = float(self.lineEdit_9.text() or 0)
            total_time_maxim = (
                self.calculate_time(swim_speed_maxim, SWIM_DISTANCE / 60) +
                self.calculate_time(bike_speed_maxim, BIKE_DISTANCE) * 60 +
                self.calculate_time(run_speed_maxim, RUN_DISTANCE) * 60
            )
            self.lineEdit_12.setText(f"{total_time_maxim:.2f}")

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числовые значения.")

    def find_champion(self):
        try:
            # Получение общего времени для каждого участника
            time_andrey = float(self.lineEdit_10.text() or float('inf'))
            time_egor = float(self.lineEdit_11.text() or float('inf'))
            time_maxim = float(self.lineEdit_12.text() or float('inf'))

            # Определение минимального времени
            min_time = min(time_andrey, time_egor, time_maxim)

            # Определение чемпиона
            if min_time == time_andrey:
                champion = "Андрей"
            elif min_time == time_egor:
                champion = "Егор"
            else:
                champion = "Максим"

            # Вывод имени чемпиона
            self.lineEdit_13.setText(champion)

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пожалуйста, сначала рассчитайте общее время.")

    @staticmethod
    def calculate_time(speed, distance):
        if speed == 0:  # Защита от деления на ноль
            return float('inf')
        return distance / speed


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TriathlonApp()
    window.show()
    sys.exit(app.exec_())