#Ejercicio 1

from decimal import Decimal

lista = ["manzana", "banana", "pera"]
print(lista)

tupla = ("rojo", "verde", "azul")
print(tupla)

float = 5.7
print(float)

entero = 10
print(entero)

decimal = Decimal(3.14) * 3
print(decimal)

diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
print(diccionario)

# ejercicio 2

import math
print(math.ceil(float))

# ejercicio 3

print(math.sqrt(float))

# ejercicio 4

primer_elemento = list(diccionario.items())[0]
print(primer_elemento)

# ejercicio 5

segundo = tupla[1]
print(segundo)

# ejercicio 6

lista.append("naranja")
print(lista)

# Ejercicio 7

lista[0] = "melon"
print(lista)

#ejercicio 8

lista.sort()
print(lista)

# Ejercicio 9

tupla  += ("amarillo",)
print(tupla)