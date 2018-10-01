#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multiplicacion(self, op1, op2):
        return op1 * op2

    def division(self, op1, op2):
        if op2 == 0:
            exit('Division by zero is not allowed')
        else:
            return op1 / op2


if __name__ == '__main__':
    operador1 = float(sys.argv[1])
    operador2 = float(sys.argv[3])
    operacion = sys.argv[2]
    calcula = CalculadoraHija()
    if operacion == 'suma':
        print(calcula.suma(operador1, operador2))
    elif operacion == 'resta':
        print(calcula.resta(operador1, operador2))
    elif operacion == 'multiplica':
        print(calcula.multiplicacion(operador1, operador2))
    elif operacion == 'divide':
        print(calcula.division(operador1, operador2))
