import parametros_generales as pg
from random import randint, uniform
import inventario as inv
def mapeo (datos, i, j):
    
    cont = 0
    if datos[i][j] == "O" or datos[i][j] == "R":
        
        if i == 0:
            if j == 0:
                #Se asume que ningun campo iniciara en los bordes del mapa
                if datos[i+1][j+1] == "C":
                    ubicacion = pg.imagenes_campo["Esquina_superior_d"]
                else:                           
                    cont = 1
            elif j == len(datos[i]) - 1:
                if datos[i+1][j-1] == "C":
                    ubicacion = pg.imagenes_campo["Esquina_superior_i"]
                else:
                    cont = 1
            else:
                if datos[i+1][j] == "C":
                    ubicacion = pg.imagenes_campo["Borde_superior_3"]
                elif datos[i+1][j] == "O" or datos[i+1][j] == "R":
                    if datos[i+1][j+1] == "C":
                        ubicacion = pg.imagenes_campo["Esquina_superior_d"]
                    elif datos[i+1][j-1] == "C":
                        ubicacion = pg.imagenes_campo["Esquina_superior_i"]
                    else:
                        cont = 1
                else:
                    cont = 1
        elif i == len(datos) - 1:
            if j == 0:
                if datos[i-1][j+1] == "C":
                    ubicacion = pg.imagenes_campo["Esquina_inferior_d"]
                else:
                    cont = 1
            elif j == len(datos[i]) - 1:
                if datos[i-1][j-1] == "C":
                    ubicacion = pg.imagenes_campo["Esquina_inferior_i"]
                else:
                    cont = 1
            else:
                if datos[i-1][j] == "C":
                    ubicacion = pg.imagenes_campo["Borde_inferior_1"]
                elif datos[i-1][j] =="R" or datos[i-1][j] == "O":
                    if datos[i-1][j+1] == "C":
                        ubicacion = pg.imagenes_campo["Esquina_inferior_d"]
                    elif datos[i-1][j-1] == "C":
                        ubicacion = pg.imagenes_campo["Esquina_inferior_i"]
                    else:
                        cont = 1  
                else:
                    cont = 1
        elif j == 0:
            if datos[i][j+1] == "C":
                ubicacion = pg.imagenes_campo["Borde_derecho_1"]
            else:
                cont = 1
        elif j == len(datos[i]) - 1:
            if datos[i][j-1] == "C":
                ubicacion = pg.imagenes_campo["Borde_Izquierdo_1"]
            else:
                cont = 1
        else:
            if datos[i][j-1] == "C":
                ubicacion = pg.imagenes_campo["Borde_derecho_1"]
            elif datos[i][j+1] == "C":
                ubicacion = pg.imagenes_campo["Borde_Izquierdo_1"]
            elif datos[i+1][j] == "C":
                ubicacion = pg.imagenes_campo["Borde_superior_3"]
            elif datos[i-1][j] == "C":
                ubicacion = pg.imagenes_campo["Borde_inferior_1"]
            elif datos[i+1][j-1] =="C":
                ubicacion = pg.imagenes_campo["Esquina_superior_i"]
            elif datos[i+1][j+1] == "C":
                ubicacion = pg.imagenes_campo["Esquina_superior_d"]
            elif datos[i-1][j+1] == "C":
                ubicacion = pg.imagenes_campo["Esquina_inferior_d"]
            elif datos[i-1][j-1] == "C":
                ubicacion = pg.imagenes_campo["Esquina_inferior_i"]
            else:
                cont = 1
        if cont == 1:
            uniforme = uniform(0,1)
            if uniforme <= 0.02 and uniforme > 0.01:
                numero = randint(1,3)
            elif uniforme <= 0.01:
                numero = 5
            else:
                numero = 4 
            ubicacion = pg.imagenes_campo["Pasto_" + str(numero)]


    elif datos[i][j] == "C":
        ubicacion = pg.imagenes_campo["Zona_siembra_3"]
    elif datos[i][j] == "H" or datos[i][j] == "T":
        ubicacion = pg.imagenes_campo["Pasto_4"]
    return ubicacion
    
    

