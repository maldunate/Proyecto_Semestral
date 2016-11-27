#! /usr/bin/env python
# encoding: UTF-8

import sys
import numpy as np
import os
from Grilla import Grilla
from Recorrido import Recorrido
from Parada import Parada
from Servicio import Servicio
from ManejoDeArchivos import ManejoDeArchivos

  
def main():
    print("Hello world!")
    nEscenario = 1
    grilla = leerArchivos(nEscenario)
    
    attrs = vars(grilla)
    print(', '.join("%s: %s" % item for item in attrs.items()))

    raw_input("enter something")
   

#flujo que lee todos los archivos usando la clase ManejoDeArchivos y retorna la grilla que posee los servicios y 
def leerArchivos(nEscenario):
    pathValoresTiempo = "..\data\Escenarios\Escenario_" + str(nEscenario) + r"\valores_tiempo.txt"
    pathTiemposDetencion = "..\data\Escenarios\Escenario_" + str(nEscenario) + r"\tiempos_detencion.txt"
    pathTiemposTransbordo = "..\data\Escenarios\Escenario_" + str(nEscenario) + r"\tiempos_transbordo.txt"
    pathCoordenadas = "..\data\Escenarios\Escenario_" + str(nEscenario) + r"\coordenadas.txt"
    pathK = "..\data\Escenarios\Escenario_" + str(nEscenario) + r"\k.txt"
    pathRecorridos = "..\data\Escenarios\Escenario_" + str(nEscenario) + r"\servicios.txt"
    pathVehiculos = "..\data\Escenarios\Escenario_" + str(nEscenario) + r"\vehiculos.txt"
    pathMatrizViajes = "..\data\Escenarios\Escenario_" + str(nEscenario) + r"\matriz_viajes.txt"


    valorK = ManejoDeArchivos.leerK(pathK)
    valores_tiempo = ManejoDeArchivos.leerValoresTiempo(pathValoresTiempo)
    grilla = Grilla(float(valores_tiempo[0]), float(valores_tiempo[1]), float(valores_tiempo[2]), float(valorK))
    tiemposDetencion = ManejoDeArchivos.leerTiemposDetencion(pathTiemposDetencion)
    tiemposTransbordo = ManejoDeArchivos.leerTiemposTransbordo(pathTiemposTransbordo)
    coordenadas = ManejoDeArchivos.leerCoordenadas(pathCoordenadas)
    #id_parada, coordenadaX, coordenadaY, tiempo_detencion, tiempo_trasbordo
    paradas = []

    for i in xrange(0,len(tiemposDetencion)):
        parada = Parada(i, float(coordenadas[2*i]), float(coordenadas[2*i+1]), float(tiemposDetencion[i]), float(tiemposTransbordo[i]))
        paradas.append(parada)
        pass

    recorridos = ManejoDeArchivos.leerRecorridos(pathRecorridos)
    vehiculos = ManejoDeArchivos.leerVehiculos(pathVehiculos)
    listaMatricesTiempo = []

    for i in xrange(0,len(vehiculos)):
        nMatrizTiempo = i
        pathMatrizTiempo = "..\data\Escenarios\Escenario_" + str(nEscenario) + "\matriz_tiempos_" + str(nMatrizTiempo) + ".txt"
        listaMatricesTiempo.append(ManejoDeArchivos.leerMatrizTiempos(pathMatrizTiempo))
        pass

    listaMatricesTiempo = matrizStrtoFloat(listaMatricesTiempo, 3)
    matrizViajes = matrizStrtoFloat(ManejoDeArchivos.leerMatrizViajes(pathMatrizViajes), 2)
    
    #id_servicio, vehiculos, matrizTiempos, recorrido
    listaServicios = []
    for i in xrange(0, len(vehiculos)):
        listaServicios.append(Servicio(i, int(vehiculos[i]), listaMatricesTiempo[i], recorridos[i]))
        pass

    grilla.setMatrizViajes(matrizViajes)
    grilla.setServicios(listaServicios)
    grilla.setListaParadas(paradas)

    return grilla


def matrizStrtoFloat(matriz, dimensiones):
    if(matriz != None):
        if(dimensiones == 3):
            for i in xrange(0, len(matriz)):
                if(matriz[0] != None):
                    for j in xrange(0, len(matriz[0])):
                        if(matriz[0][0] != None):
                            for k in xrange(0, len(matriz[0][0])):
                                matriz[i][j][k] = float(matriz[i][j][k])
                                pass
                        pass
                pass
        elif (dimensiones == 2):
            for i in xrange(0, len(matriz)):
                if(matriz[0] != None):
                    for j in xrange(0, len(matriz[0])):
                        matriz[i][j] = float(matriz[i][j])
                        pass
                pass
        elif (dimensiones == 1):
            for i in xrange(0, len(matriz)):
                matriz[i] = float(matriz[i])
                pass
    return matriz

if __name__ == '__main__':
    main()
