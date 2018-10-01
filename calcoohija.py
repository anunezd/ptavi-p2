#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multiplicacion(self):
        return self.operador1 * self.operador2

    def division(self):
        if operador2 == 0:
            exit('Division by zero is not allowed')
        else:
            return self.operador1 / self.operador2


if __name__ == '__main__':
    operador1 = float(sys.argv[1])
    operador2 = float(sys.argv[3])
    operacion = sys.argv[2]
    calcula = CalculadoraHija(operador1, operador2)
    if operacion == 'suma':
        print(calcula.suma())
    elif operacion == 'resta':
        print(calcula.resta())
    elif operacion == 'multiplica':
        print(calcula.multiplicacion())
    elif operacion == 'divide':
        print(calcula.division())
