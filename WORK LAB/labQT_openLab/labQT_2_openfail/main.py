import os
from PyQt5 import QtCore, QtGui, QtWidgets

from form_labQT_2 import Ui_Form

class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.buttonBox.accepted.connect(self.open_file)
        self.buttonBox_2.rejected.connect(self.close)
    
    def open_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Выберите файл', '', 'Все файлы (*.*)'
        )
        
        if file_path:
            filename = os.path.basename(file_path)
            extension = os.path.splitext(filename)[1]
            creation_time = os.path.getctime(file_path)
            modification_time = os.path.getmtime(file_path)
            self.label_7.setText(filename)
            self.label_8.setText(extension)
            self.label_9.setText(str(creation_time))
            self.label_10.setText(str(modification_time))
            self.label_11.setText('Автор')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())