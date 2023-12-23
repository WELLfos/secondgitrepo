from PyQt5.QtCore import Qt
import random
from PyQt5 import uic
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __int__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.button_play.clicked.connect(self.create_yellow_circle)

        self.radius = 0

    def create_yellow_circle(self):
        self.radius = random.randint(50, 200)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(100, 100, 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
