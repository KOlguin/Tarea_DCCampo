from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.Qt import QTest
import parametros_generales as pg
import parametros_acciones as pa



class Character(QObject):
    """
    Clase que se encargará de manejar los datos internos del personaje.
    Es parte del back-end del programa, al contener parte de la lógica.
    """

    update_character_signal = pyqtSignal(str)

    def __init__(self, x, y, ancho, largo, ancho_pixel, largo_pixel):
        super().__init__()
        # Datos iniciales
        self.direction = 'R'
        self._x = x
        self._y = y
        self.initial_y = y
        self.ancho = ancho
        self.largo = largo
        self.ancho_pixel = ancho_pixel
        self.largo_pixel = largo_pixel
        self.dinero = pg.MONEDAS_INICIALES

        print(self.ancho_pixel, self.largo_pixel, self.ancho, self.largo)
        #self.ancho_pixel, self.largo_pixel = funcion_N()
        # Se inicializa nula la señal de actualizar la interfaz
        self.update_window_signal = None

        # Se conecta la señal de actualizar datos del personaje
        self.update_character_signal.connect(self.move)

    def update_window_character(self, position='stand'):
        """
        Envía los datos del personaje mediante una señal a la
        interfaz para ser actualizados.
        :param position: str
        :return: None
        """
        if self.update_window_signal:
            self.update_window_signal.emit({
                'x': self.x,
                'y': self.y,
                'direction': self.direction,
                'position': position
            })

  

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        """
        Chequea que la coordenada x se encuentre dentro los límites
        y envía la señal de actualización a la interfaz.
        :param value: int
        :return: None
        """
        if 30 < value < self.largo + 30:
            self._x = value
            self.update_window_character('walk')
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        """
        Chequea que la coordenada x se encuentre dentro los límites
        y envía la señal de actualización a la interfaz.
        :param value: int
        :return: None
        """
        if 190 < value < 620 - (620 - (165 + self.ancho)):
            self._y = value
            self.update_window_character('walk')


    def move(self, event):
        """
        Función que maneja los eventos de movimiento desde la interfaz.
        :param event: str
        :return: None
        """
        if event == 'R':
            self.direction = 'R'
            self.x += self.largo_pixel
        elif event == 'L':
            self.direction = 'L'
            self.x -= self.largo_pixel
        elif event == "U":
            self.direction = 'U'
            self.y -= self.ancho_pixel
        elif event == "D":
            self.direction = "D"
            self.y += self.ancho_pixel

    #def get_position(self, )
   