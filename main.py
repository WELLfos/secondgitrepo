from PyQt5.QtCore import Qt
import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __int__(self):
        super().__init__()
        self.setupUi()
        self.button_play.clicked.connect(self.create_yellow_circle)
        self.radius = random.randint(50, 200)

    def create_yellow_circle(self):
        self.radius = random.randint(50, 200)
        self.update()

    def paintEvent(self, event):
        self.radius = random.randint(50, 200)
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        painter.drawEllipse(100, 100, self.radius, self.radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())