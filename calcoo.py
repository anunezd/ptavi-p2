#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def suma(self, op1, op2):
        return op1 + op2

    def resta(self, op1, op2):
        return op1 - op2


if __name__ == '__main__':
    operador1 = float(sys.argv[1])
    operador2 = float(sys.argv[3])
    operacion = sys.argv[2]
    calcula = Calculadora()
    if operacion == 'suma':
        print(calcula.suma(operador1, operador2))
    elif operacion == 'resta':
        print(calcula.resta(operador1, operador2))
