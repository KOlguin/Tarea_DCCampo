import sys
import os
from PyQt5.QtWidgets import QListWidget, QMainWindow, QGroupBox, QGridLayout, QHBoxLayout, QVBoxLayout, QWidget, QMessageBox, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont #Permite trabajar con fuentes  
from PyQt5.QtCore import QMimeData, Qt, QEvent, QRect, QSize
from PyQt5.QtGui import QDrag, QPixmap, QPainter
from PyQt5 import uic
import parametros_generales as pg
from random import randint, uniform

class DraggableLabel(QLabel):
    def __init__(self, parent):#, tipo):
        super(QLabel, self).__init__(parent)
        self.setPixmap(QPixmap(os.path.join("recursos", "artichoke.png")))
        self.setGeometry(60, 35, 40, 30)
        self.setStyleSheet("background: transparent")
        self.setScaledContents(True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        self.show()
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drag_start_position = e.pos()
    
    def mouseMoveEvent(self, e):
        if not (e.buttons() & Qt.LeftButton):
            return
        if (e.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        mimedata.setImageData(self.pixmap().toImage())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(e.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)
class DropLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
        self.setStyleSheet("background: transparent")

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            print('event accepted')
            event.accept()
        else:
            print('event rejected')
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage():
            self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))
