#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

with open(sys.argv[1], newline='') as csvfile:
    listas = csv.reader(csvfile)
    for lista in listas:
        lista_float = list(map(float, lista[1:]))
        operacion = lista[0]
        c = calcoohija.CalculadoraHija()
        if operacion == 'suma':
            r = c.suma(lista_float[0], lista_float[1])
            for elemento in lista_float[2:]:
                r = c.suma(r, elemento)
            print(r)

        if operacion == 'resta':
            r = c.resta(lista_float[0], lista_float[1])
            for elemento in lista_float[2:]:
                r = c.resta(r, elemento)
            print(r)

        if operacion == 'multiplica':
            r = c.multiplicacion(lista_float[0], lista_float[1])
            for elemento in lista_float[2:]:
                r = c.multiplicacion(r, elemento)
            print(r)

        if operacion == 'divide':
            r = c.division(lista_float[0], lista_float[1])
            for elemento in lista_float[2:]:
                r = c.division(r, elemento)
            print(r)
