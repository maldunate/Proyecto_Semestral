#!/usr/bin/env python

class Servicio:
    #"""docstring for Servicios"""
    def __init__(self, id_servicio, vehiculos, matrizTiempos, recorrido):
        #super(Servicio, self).__init__()
        self.id_servicio = id_servicio
        self.vehiculos = vehiculos
        self.matrizTiempos = matrizTiempos
        self.recorrido = self.recorridoToInt(recorrido)
        

    def recorridoToInt(self, recorrido):
        if(recorrido != None):
            for i in xrange(0, len(recorrido)):
                recorrido[i] = int(recorrido[i])
                pass
        return recorrido