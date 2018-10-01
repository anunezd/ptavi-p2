#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def __init__(self, op1, op2):
        self.operador1 = op1
        self.operador2 = op2

    def suma(self):
        return self.operador1 + self.operador2

    def resta(self):
        return self.operador1 - self.operador2


if __name__ == '__main__':
    operador1 = float(sys.argv[1])
    operador2 = float(sys.argv[3])
    operacion = sys.argv[2]
    calcula = Calculadora(operador1, operador2)
    if operacion == 'suma':
        print(calcula.suma())
    elif operacion == 'resta':
        print(calcula.resta())
