from datetime import datetime
from time import strftime
from math import sqrt
import time
import os
import sys

"""
Calculadora em Python
"""

print("\n" * 15)

print("\n*****Python Calculator*****")

escolha = 0


# funçoes da calculadora

def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def potencia(a, b):
    return a ** b


# Imprimindo a data atual para usuario
print("\n")
t1 = time.strftime('%D, %H:%M:%S')
print(t1)

print("\nSelecione a opção desejada:")

# opções do usuário
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")

# Solicitando a opção desejada ao usuário

while escolha < 1 or escolha > 5:
    try:
        escolha = int(input("\nQual é a opção? (1, 2, 3, 4, 5): "))
    except ValueError:
        print("Você não digitou um número!")


# Solicitando os números ao usuário,
num1 = float(input("Qual o primeiro número?: "))
num2 = float(input("Qual o segundo número?: "))


if escolha == 1:
    print("\n")
    print("O resultado da somatória é:", num1, '+', num2, '=', soma(num1, num2))
    print("\n")

if escolha == 2:
    print("\n")
    print("O resultado da subtração é:", num1, '-', num2, '=', subtracao(num1, num2))
    print("\n")

if escolha == 3:
    print("\n")
    print("O resultado da multiplicação é:", num1, '*', num2, '=', multiplicacao(num1, num2))
    print("\n")

if escolha == 4:
    print("\n")
    print("O resultado da divisão é:", num1, '/', num2, '=', divisao(num1, num2))
    print("\n")

if escolha == 5:
    print("\n")
    print("O resultado da potencialização é:", num1, '**', num2, '=', potencia(num1, num2))
    print("\n")

# imprimindo novamente a data para o usuario após a finalizaçao da operacao
t2 = time.strftime('%D, %H:%M:%S')
print(t2)

# Reiniciando ou finalizando
restart = input("\nDeseja calcular novamente? [sim/nao] > ")

if restart == "sim":
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
else:
    print("\nObrigado, estamos fechando a calculadora!")
    sys.exit(0)
