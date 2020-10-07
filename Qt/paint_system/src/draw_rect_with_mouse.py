import sys

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

        self.left_top = QPoint()
        self.right_bottom = QPoint()
        self.isDrawing = False

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(Qt.red, 3, Qt.SolidLine))
        rect = QRect(self.left_top, self.right_bottom)
        painter.drawRect(rect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.left_top = event.pos()
            self.right_bottom = event.pos()
            self.isDrawing = True

    def mouseMoveEvent(self,event):
        if event.buttons() ==  Qt.LeftButton and self.isDrawing:
            self.right_bottom = event.pos()
            self.update()

    def mouseReleaseEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.isDrawing = False


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Drawing a rectangle on image with mouse")
        self.setMinimumSize(640, 480)

        self.label = MyLabel(self)
        self.label.setGeometry(QRect(0, 0, 300, 300))

        #QImage = QtGui.QImage("kaka.jpg")
        img = cv2.imread('../images/kaka.jpg')
        img = cv2.resize(img, (300, 300))
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImage = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)

        pixmap = QtGui.QPixmap.fromImage(QImage)
        self.label.setPixmap(pixmap)
        self.label.setCursor(Qt.CrossCursor)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
