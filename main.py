import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.label.setText(self.textEdit.toPlainText())  # текст читаем
        self.tabWidget.addTab(QLabel("кто прочитал тот здохнет"), "тыкни сюды")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())