import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsItem
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt, QRectF

class RectangleDrawer(QGraphicsView):
    def __init__(self):
        super(RectangleDrawer, self).__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.rect_item = None
        self.start_point = None
        self.end_point = None

        self.pen = QPen(Qt.red, 2)

        self.setSceneRect(0, 0, 800, 600)  # Set scene rectangle size

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()
            self.end_point = event.pos()

            if self.rect_item:
                self.scene.removeItem(self.rect_item)

            self.rect_item = QGraphicsRectItem()
            self.rect_item.setPen(self.pen)
            self.scene.addItem(self.rect_item)
            self.rect_item.setRect(QRectF(self.start_point, self.end_point))

    def mouseMoveEvent(self, event):
        if self.start_point is not None:
            self.end_point = event.pos()
            self.rect_item.setRect(QRectF(self.start_point, self.end_point))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_point = event.pos()
            self.rect_item.setRect(QRectF(self.start_point, self.end_point))
            self.start_point = None
            self.end_point = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RectangleDrawer()
    window.show()
    sys.exit(app.exec_())