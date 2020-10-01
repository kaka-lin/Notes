import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Drawing a Rectangle")
        self.setMinimumSize(640, 480)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(Qt.red, 5, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(Qt.green, Qt.DiagCrossPattern))
        painter.drawRect(270, 190, 100, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
