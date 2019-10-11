from os import path
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import pyqtSignal, Qt, QTimer, QTime, QThread
from PyQt5.QtTest import QTest
from character import Character
import inventario as inv
import parametros_generales as pg
from random import uniform, randint
#import clock
from time import sleep
from mapeo import mapeo
import Tienda as st

class LabelClick(QLabel):
    clicked = pyqtSignal(str)
    def __init__(self, parent = None):
        super(LabelClick, self).__init__(parent)
    
    def mousePressEvent(self, e):
        self.ultimo = "Click"
    
    def mouseReleaseEvent(self, e):
        if self.ultimo == "Click":
            self.clicked.emit(self.ultimo)
"""
class Dia(QThread):
    update_day = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        #print("NOOOO")
        self.time = 1
        #self.crear_dias()
        #self.crear_dias()
    
    def run(self):
        while True:
            print("Entra")
            QTest.qWait(10000)
            self.Paso_dias()
    
    def Paso_dias(self):
        print("Funciono")
        self.time += 1
        self.update_day.emit(clase)
    #def crear_dias(self):
    #    self.dia = QLabel(str(self.time), self)
"""
class GameWindow(QWidget):
    
    update_window_signal = pyqtSignal(dict)
    show_game_signal = pyqtSignal()
    #update_day = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        # Se instancia el personaje del backend
        self._frame = 1
        self.background = None
        self.front_character = None
        self.current_sprite = None
        self.update_character_signal = None
        self.update_store = None
        self.datos_2 = []
        self.init_gui()
        self.backend_character = Character(35, 485, self.ancho*self.ancho_pixel,\
             self.largo*self.largo_pixel, self.ancho_pixel, self.largo_pixel)
        self.front_character = QLabel(self)
        self.current_sprite = QPixmap(pg.sprite_personaje[('stand')])
        self.front_character.setPixmap(self.current_sprite)
        self.front_character.setStyleSheet("background: transparent")
        #self.front_character.resize(largo_pixel//2, ancho_pixel)
        #self.front_character.setScaledContents(True)
        self.front_character.move(35, 485)
        self.Tienda = None
        
        self.init_signals()
        #self.dia = None
        #self.crear_dias()
        #self.crear_dias()
        #self.dia.text = 'change the value'
        #self.dia.setGeometry(900, 170, 120, 30)
        #self.dia.setFont(QFont("Times New Roman", 18))
        #self.dia.setStyleSheet("background: transparent") 
        #self.clock = QTimer()
        
        #self.clock.timeout.connect(self.random_trees)
        #self.clock.start(10)
    
    def init_gui(self):
        self.setGeometry(200, 40, 1100, 680)
        self.setWindowTitle("Prueba_2")
        self.setStyleSheet("background-color: #97ff67")
        self.label1 = QLabel(self)
        self.label1.setGeometry(10, 10, 850, 150)
        self.label1.setPixmap(QPixmap(path.join("otros", "invetary_template.jpg")))
        self.label1.setScaledContents(True)
        label_to_drag = inv.DraggableLabel(self)
        self.label2 = QLabel("Stats", self)
        self.label2.setGeometry(870, 10, 211, 660)
        self.label2.setPixmap(QPixmap(path.join("otros", "window_template.jpg")))
        self.label2.setScaledContents(True)
        self.stats = QLabel("Stats:", self)
        self.stats.setGeometry(900, 70, 141, 51)
        self.stats.setFont(QFont("Times New Roman", 24, QFont.Black))
        self.stats.setStyleSheet("background: transparent")
        self.background = QLabel(self)
        self.background.setGeometry(10, 170, 850, 500)
        self.background.setPixmap(QPixmap(path.join("otros", "window_template.jpg")))
        self.background.setScaledContents(True)
        self.ancho_pixel = 0
        self.largo_pixel = 0
        self.ancho = 0
        self.largo = 0
        self.time = 1
        #self.pass_day = Dia()
        self.crear_dias()
        #self.crear_dias()
        self.dia.text = 'change the value'
        #self.dia.setGeometry(900, 170, 120, 30)
        #self.dia.setFont(QFont("Times New Roman", 18))
        #self.dia.setStyleSheet("background: transparent")
        self.leer_mapa()
          
    def init_signals(self):
        # Se conecta la señal para abrir esta ventana con el método show
        self.show_game_signal.connect(self.show)
        # Se conecta la señal de actualización con un método
        self.update_window_signal.connect(self.update_window)
        # Define la señal que actualizará el personaje en back-end
        self.update_character_signal = self.backend_character.update_character_signal
        # Se le asigna al back-end la señal para actualizar esta ventana
        self.backend_character.update_window_signal = self.update_window_signal
        #self.barra.connect(bar.progres)
        #self.pass_day.start()
    
    def crear_dias(self):
        self.dia = QLabel("Dia: " + str(self.time), self)
        #self.dia.text = 'change the value'
        self.dia.setGeometry(900, 170, 120, 30)
        self.dia.setFont(QFont("Times New Roman", 18))
        self.dia.setStyleSheet("background: transparent")
    
    def pasar_dias(self):
        print("Paso dia")
        self.time += 1
        self.dia.setText("Dia:" + str(self.time))
        return self.time
    """
    def run(self):
        while True:
            print("NOOOO")
            QTest.qWait(3)
            self.Paso_dias()
    """

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        self._frame = value if value < 5 else 1

    key_event_dict = {
        Qt.Key_D: 'R',
        Qt.Key_A: 'L',
        Qt.Key_W: 'U',
        Qt.Key_S: 'D'
    }

    def keyPressEvent(self, event):

        if event.key() in self.key_event_dict:
            action = self.key_event_dict[event.key()]
            self.update_character_signal.emit(action)


    def update_window(self, event):
        
        #print("Hola", self.clock)
        direction = event['direction']
        position = event['position']
        if position == 'walk':
            self.frame += 1
            self.current_sprite = QPixmap(pg.sprite_personaje[(position, direction, self.frame)])

        else:
            self.frame += 1
            self.current_sprite = QPixmap(pg.sprite_personaje[(position, self.frame)])
        
        self.front_character.setPixmap(self.current_sprite)
        self.front_character.move(event['x'], event['y'])
    
    def leer_mapa(self):
        ruta = open("mapas/mapa_1.txt", "r", encoding="utf-8")
        datos_1 = []
        for linea in ruta:
            datos_1.append(linea.strip("\n"))
        for i in range (0, len(datos_1)):
            self.datos_2.append(datos_1[i].split(" "))
        self.mapeo()
    
    def on_click(self, event):
     print('Click')
     if event.button() == Qt.LeftButton:
        pass
    
    def mapeo(self):
        self.ancho += len(self.datos_2)
        self.largo += len(self.datos_2[0])
        inicio_w = 30
        inicio_h = 190
        ancho_pixel, largo_pixel = pg.funcion_N(self.ancho, self.largo)
        print(ancho_pixel, largo_pixel)
        self.ancho_pixel += ancho_pixel
        self.largo_pixel += largo_pixel

        for i in range(0, len(self.datos_2)):
            for j in range(0, len(self.datos_2[i])):
                label_mapa = mapeo(self.datos_2, i, j)
                if self.datos_2[i][j] == "R":
                    label_1 = QLabel(self)
                    label_1.setPixmap(QPixmap(path.join("mapa", label_mapa)))
                    label_1.setScaledContents(True)
                    label_1.setGeometry(inicio_w + j*largo_pixel, inicio_h + i*ancho_pixel,\
                         largo_pixel, ancho_pixel)                
                    libre = path.join("mapa", pg.imagenes_campo["Roca"])
                    label = QLabel(self)
                    label.setPixmap(QPixmap(libre))
                    label.setStyleSheet("background: transparent")
                    label.setScaledContents(True)
                    label.setGeometry(inicio_w + j*largo_pixel, inicio_h + i*ancho_pixel,\
                         largo_pixel, ancho_pixel)
                elif self.datos_2[i][j] == "C":
                    libre = path.join("mapa", label_mapa)
                    label = inv.DropLabel(self)
                    label.setPixmap(QPixmap(libre))
                    label.setGeometry(inicio_w + j*largo_pixel, inicio_h + i*ancho_pixel,\
                         largo_pixel, ancho_pixel)
                    label.setScaledContents(True)
                else:
                    libre = path.join("mapa", label_mapa)
                    label = QLabel(self)
                    label.setPixmap(QPixmap(libre))
                    label.setGeometry(inicio_w + j*largo_pixel, inicio_h + i*ancho_pixel,\
                         largo_pixel, ancho_pixel)
                    label.setScaledContents(True)
        
        house = 0
        store = 0
        for i in range (0,len(self.datos_2)):
            for j in range (0, len(self.datos_2[i])):
                #Linea 91 y 99 sacado de https://stackoverflow.com/questions/7667552/qt-widget-with-transparent-background
                if self.datos_2[i][j] == "H" and house == 0:
                    casa = QLabel(self)
                    libre = path.join("mapa", pg.imagenes_campo["casa"])
                    casa.setPixmap(QPixmap(libre))
                    casa.setScaledContents(True)
                    casa.setStyleSheet("background: transparent")
                    casa.setGeometry(inicio_w + j*largo_pixel, inicio_h + i*ancho_pixel,\
                         2*largo_pixel, 2*ancho_pixel)
                    house = 1
                    break
                if self.datos_2[i][j] =="T" and store == 0:
                    tienda = LabelClick(self)
                    libre = path.join("mapa", pg.imagenes_campo["tienda"])
                    tienda.setPixmap(QPixmap(libre))
                    #tienda.setIcon(QIcon(libre))
                    tienda.setStyleSheet("background: transparent")
                    tienda.setScaledContents(True)
                    tienda.setGeometry(inicio_w + j*largo_pixel, inicio_h + i*ancho_pixel,\
                         2*largo_pixel, 2*ancho_pixel)
                    tienda.clicked.connect(self.Clic)
                    store = 1
                    break
            if house == 1 and store == 1:
                break
    def Clic (self, accion):
        self.Tienda = st.Tienda()
    """    
    def random_trees(self):
        arbol = QLabel(self)
        arbol.setPixmap(QPixmap("otros", "tree.png"))
        x = randint(100, 500)
        y = randint(100, 500)
        arbol.setGeometry(x, y, 50, 50)
        arbol.setScaledContents(True)
    """