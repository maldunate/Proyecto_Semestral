#!/usr/bin/env python

import sys
import numpy as np
import os

class ManejoDeArchivos:

    @staticmethod
    def leer(path):
        archivo = open(path, "r")
        contenido = archivo.read()
        return contenido

    @staticmethod
    def generarPath(pathRelativo):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        path = os.path.join(fileDir, pathRelativo)
        path = os.path.abspath(os.path.realpath(path))
        return path

    @staticmethod
    def leerValoresTiempo(r):
       #archivo valor tiempo 
        s = ManejoDeArchivos.leer(ManejoDeArchivos.generarPath(r)).split()
        return s

    @staticmethod
    def leerK(r):
       #archivo valor tiempo 
        s = ManejoDeArchivos.leer(ManejoDeArchivos.generarPath(r))
        return s

    @staticmethod
    def leerTiemposDetencion(r):
        #paradas
        listaTiemposDetencion = ManejoDeArchivos.leer(ManejoDeArchivos.generarPath(r)).split()
        return listaTiemposDetencion

    @staticmethod
    def leerTiemposTransbordo(r):
        #paradas
        listaTiemposTransbordo = ManejoDeArchivos.leer(ManejoDeArchivos.generarPath(r)).split()
        return listaTiemposTransbordo

    @staticmethod
    def leerCoordenadas(r):
        #paradas
        listaCoordenadas = ManejoDeArchivos.leer(ManejoDeArchivos.generarPath(r)).split()
        return listaCoordenadas

    @staticmethod
    def leerRecorridos(r):
        #paradas
        listaRecorridos = ManejoDeArchivos.leer(ManejoDeArchivos.generarPath(r)).split("\n")
        lista = []
        for i in xrange(0,len(listaRecorridos)):
            lista.append(listaRecorridos[i].split())
            pass

        return lista

    @staticmethod
    def leerVehiculos(r):
        #paradas
        listaVehiculos = ManejoDeArchivos.leer(ManejoDeArchivos.generarPath(r)).split()
        return listaVehiculos

    @staticmethod
    def leerMatrizTiempos(r):
        #paradas
        fila = ManejoDeArchivos.leer(ManejoDeArchivos.generarPath(r)).split("\n")
        lista = []
        for i in xrange(0,len(fila)):
            lista.append(fila[i].split())
            pass

    @staticmethod
    def leerMatrizViajes(r):
        #paradas
        fila = ManejoDeArchivos.leer(ManejoDeArchivos.generarPath(r)).split("\n")
        lista = []
        for i in xrange(0,len(fila)):
            lista.append(fila[i].split())
            pass
        # matriz = []
        # for i in xrange(0,len(lista)):
        #     matriz.append(lista[i].split())
        #     pass

        return lista
    
    @staticmethod
    def escribirMatriz(nombreDoc, matriz):
        path = r"..\output\\" + nombreDoc + ".txt"
        archivo = open(path, "w")
        string = ""
        for i in xrange(0, len(matriz)):
            if(i != 0 && i != len(matriz)):
                archivo.write("\n")
            for j in xrange(0, len(matriz[0])):
                string = ""
                if(j != len(matriz[0])):
                    string = str(matriz) + "\t"
                else
                    string = str(matriz)
                    
                archivo.write(string)
                pass
            pass
