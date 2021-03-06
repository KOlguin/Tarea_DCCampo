from os import path
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QDialog, QApplication, QPushButton
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import pyqtSignal, QSize, Qt, QTimer, QTime
from character import Character
import inventario as inv
import parametros_generales as pg
from random import uniform, randint
import parametros_precios as pp

class Tienda(QWidget):
    update_store = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.initgui()
    def initgui(self):
        self.setGeometry(100, 100, 500, 500)
        oImage = QImage("otros/window_template.jpg")
        sImage = oImage.scaled(QSize(500,500))                   
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     
        self.setPalette(palette)
        self.setWindowTitle("Tienda")
        self.Item = QLabel("Item", self)
        self.Item.setGeometry(40, 10, 47,71)
        self.Item.setFont(QFont("Times New Roman", 14))
        self.Precio = QLabel("Precio", self)
        self.Precio.setGeometry(130, 10, 47,71)
        self.Precio.setFont(QFont("Times New Roman", 14))
        self.Accion = QLabel("Accion", self)
        self.Accion.setGeometry(210, 25, 71, 41)
        self.Accion.setFont(QFont("Times New Roman", 14))
        self.Hacha = QLabel(self)
        self.Hacha.setPixmap(QPixmap(path.join("otros", "axe.png")))
        self.Hacha.setGeometry(40, 70, 47, 71)
        self.Hacha.setScaledContents(True)
        self.precio_hacha = QLabel("$" + str(pp.PRECIO_HACHA), self)
        self.precio_hacha.setFont(QFont("Times New Roman", 14))
        self.precio_hacha.setGeometry(130, 90, 41, 21)
        self.comprar_hacha = QPushButton("Comprar", self)
        self.comprar_hacha.setFont(QFont("Times New Roman", 12))
        self.comprar_hacha.setGeometry(200, 80, 75, 23)
        self.vender_hacha = QPushButton("Vender", self)
        self.vender_hacha.setFont(QFont("Times New Roman", 12))
        self.vender_hacha.setGeometry(200, 110, 75, 23)
        self.Azadera = QLabel(self)
        self.Azadera.setPixmap(QPixmap(path.join("otros", "hoe.png")))
        self.Azadera.setGeometry(40, 160, 47, 71)
        self.Azadera.setScaledContents(True)
        self.precio_azadera = QLabel("$" + str(pp.PRECIO_AZADA), self)
        self.precio_azadera.setFont(QFont("Times New Roman", 14))
        self.precio_azadera.setGeometry(130, 180, 41, 21)
        self.comprar_azadera = QPushButton("Comprar", self)
        self.comprar_azadera.setFont(QFont("Times New Roman", 12))
        self.comprar_azadera.setGeometry(200, 160, 75, 23)
        self.vender_azadera = QPushButton("Vender", self)
        self.vender_azadera.setFont(QFont("Times New Roman", 12))
        self.vender_azadera.setGeometry(200, 190, 75, 23)
        self.Alcachofa = QLabel(self)
        self.Alcachofa.setPixmap(QPixmap(path.join("recursos", "artichoke.png")))
        self.Alcachofa.setGeometry(40, 250, 47, 71)
        self.Alcachofa.setScaledContents(True)
        self.precio_alcachofa = QLabel("$" + str(pp.PRECIO_ALACACHOFAS), self)
        self.precio_alcachofa.setFont(QFont("Times New Roman", 14))
        self.precio_alcachofa.setGeometry(130, 270, 41, 21)
        self.vender_alcachofa = QPushButton("Vender", self)
        self.vender_alcachofa.setFont(QFont("Times New Roman", 12))
        self.vender_alcachofa.setGeometry(200, 270, 75, 23)
        self.Choclo = QLabel(self)
        self.Choclo.setPixmap(QPixmap(path.join("recursos", "corn.png")))
        self.Choclo.setGeometry(40, 340, 47, 71)
        self.Choclo.setScaledContents(True)
        self.precio_choclo = QLabel("$" + str(pp.PRECIO_CHOCLOS), self)
        self.precio_choclo.setFont(QFont("Times New Roman", 14))
        self.precio_choclo.setGeometry(130, 370, 41, 21)
        self.vender_choclo = QPushButton("Vender", self)
        self.vender_choclo.setFont(QFont("Times New Roman", 12))
        self.vender_choclo.setGeometry(200, 370, 75, 23)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = Tienda()
    m.show()
    sys.exit(app.exec_())
