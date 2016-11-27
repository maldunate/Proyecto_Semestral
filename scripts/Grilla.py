#!/usr/bin/env python

class Grilla:
    """docstring for Grilla"""
    def __init__(self, tViaje, tEspera, tTraslado, k):
        #super(Grilla, self).__init__()
        self.valor_tiempo_viaje = tViaje;
        self.valor_tiempo_espera = tEspera;
        self.valor_tiempo_traslado = tTraslado;
        self.k = k
        self.servicios = []
        self.listaParadas = []
        self.matrizDeViajes = []

    def setServicios(self, servicios):
        self.servicios = servicios

    def setListaParadas(self, listaParadas):
        self.listaParadas = listaParadas

    def setMatrizViajes(self, listaViajes):
        self.matrizDeViajes = listaViajes
        