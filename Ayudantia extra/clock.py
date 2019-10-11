from PyQt5 import QtCore
from PyQt5.QtTest import QTest
from time import sleep
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, QThread
class Dia(QThread):
    update_day = pyqtSignal()
    def __init__(self):
        print("NOOOO")
        self.inicio = 1
    def paso_tiempo(self):
        while True:
            QTest.qWait(6)
            self.inicio += 1
    def actualizar_dia():
        pass
    def crear_dia(self):
        time = self.paso_tiempo()
        print(time)

 
def timerEvent(time):
    time = time.addSecs(1)
    print(time.toString("hh:mm:ss"))

#def actualizar_dia():

D = Dia()
print(D.paso_tiempo())


    