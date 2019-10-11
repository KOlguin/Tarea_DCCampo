from os import path
imagenes_campo = {
    "casa": "house.png",
    "tienda": "store.png",
    "Pasto_1":"tile000.png",
    "Pasto_2": "tile001.png",
    "Pasto_3": "tile002.png",
    "Pasto_4": "tile006.png",
    "Pasto_5": "tile028.png",
    "Pasto_6": "tile029.png",
    "Roca": "tile030.png",
    "Zona_siembra_1": "tile003.png",
    "Zona_siembra_2": "tile004.png",
    "Zona_siembra_3": "tile007.png",
    "Zona_siembra_4": "tile019.png",
    "Zona_siembra_5": "tile020.png",
    "Esquina_superior_d": "tile012.png",
    "Esquina_superior_i": "tile015.png",
    "Esquina_inferior_d": "tile024.png",
    "Esquina_inferior_i": "tile027.png",
    "Borde_superior_1": "tile011.png",
    "Borde_superior_2": "tile017.png",
    "Borde_superior_3": "tile013.png",
    "Borde_inferior_1": "tile023.png",
    "Borde_inferior_2": "tile025.png",
    "Borde_inferior_3": "tile022.png",
    "Borde_derecho_1": "tile021.png",
    "Borde_Izquierdo_1": "tile018.png",
    "Otro": "tile010.png"
}
sprite_personaje = {
    ('stand'): path.join('personaje', 'down_1.png'),
    ('walk', 'R', 1): path.join('personaje', 'right_1.png'),
    ('walk', 'R', 2): path.join('personaje', 'right_2.png'),
    ('walk', 'R', 3): path.join('personaje', 'right_3.png'),
    ('walk', 'R', 4): path.join('personaje', 'right_4.png'),
    ("walk", 'L', 1): path.join('personaje', 'left_1.png'),
    ("walk", 'L', 2): path.join('personaje', 'left_2.png'),
    ("walk", 'L', 3): path.join('personaje', 'left_3.png'),
    ("walk", 'L', 4): path.join('personaje', 'left_4.png'),
    ("walk", 'U', 1): path.join('personaje', 'up_1.png'),
    ("walk", 'U', 2): path.join('personaje', 'up_2.png'),
    ("walk", 'U', 3): path.join('personaje', 'up_3.png'),
    ("walk", 'U', 4): path.join('personaje', 'up_4.png'),
    ("walk", 'D', 1): path.join('personaje', 'down_1.png'),
    ("walk", 'D', 2): path.join('personaje', 'down_2.png'),
    ("walk", 'D', 3): path.join('personaje', 'down_3.png'),
    ("walk", 'D', 4): path.join('personaje', 'down_4.png')
}

tipo_recurso = {
    "alcachofa": path.join("recursos", "artichoke.png"),
    "choclo": path.join("recursos", "corn.png"),
    "oro": path.join("recursos", "gold.png"),
    "leña": path.join("recursos", "wood.png"),
    "Hacha": path.join("otros", "axe.png"),
    "Azada": path.join("otros", "hoe.png"),
    "ticket": path.join("otros", "ticket.png")

}
def funcion_N(ancho, largo):
    """ 
    Set valores de los pixeles
    params:

    :ancho_pixel: 480 // largo de la dimensión y de la matriz del mapa
    :largo_pixel: 810 // largo de la dimensión x de la matriz del mapa

    """
    ancho_pixel = 460//ancho
    largo_pixel = 810//largo
    print(ancho_pixel, largo_pixel)

    return (ancho_pixel, largo_pixel)

MONEDAS_INICIALES = 10