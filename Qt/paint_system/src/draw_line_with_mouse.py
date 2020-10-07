import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.image = QtGui.QImage("../images/kaka.jpg")
        self.begin_position = QPoint()
        self.end_position = QPoint()
        self.drawing = False

        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Drawing line on image with mouse")
        self.setMinimumSize(640, 480)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # event.pos():
            #   returns the position of the mouse cursor
            self.begin_position = event.pos()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if event.buttons() ==  Qt.LeftButton and self.drawing:
            painter_line = QtGui.QPainter(self.image)
            painter_line.setPen(QtGui.QPen(Qt.red, 3, Qt.SolidLine))
            painter_line.drawLine(self.begin_position, event.pos())
            self.begin_position = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Release")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
