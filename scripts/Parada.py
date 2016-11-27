#!/usr/bin/env python

class Parada:
    """docstring for Parada"""
    def __init__(self, id_parada, coordenadaX, coordenadaY, tiempo_detencion, tiempo_trasbordo):
        #super Parada, self).__init__()
        self.id_parada = id_parada
        self.X = coordenadaX
        self.Y = coordenadaY
        self.tiempo_detencion = tiempo_detencion
        self.tiempo_trasbordo = tiempo_trasbordo