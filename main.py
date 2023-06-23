# Ejercicio 9.2 Python - Open Bootcamp
from functools import reduce

lista = list(range(1020))
def par(num):
    return num % 2
def suma(a, b):
    return a + b

def app(lista):
    resultado = list(filter(par, lista))
    resultado = reduce(suma, resultado)

    print(resultado)

if __name__ == '__main__':
    #print(lista)

    app(lista)
