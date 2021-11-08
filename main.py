"""Ejercicio 6"""

import statistics
lista_numeros = list()
while True:
    numeros = float(input("Introduce los números de los que quieres hacer los cálculos: "))
    if numeros == 100:
        break
    lista_numeros.append(numeros)

media = statistics.mean(lista_numeros)
mediana = statistics.median(lista_numeros)
varianza = statistics.variance(lista_numeros)

print("Media: ", media, "\nMediana:", mediana, "\nVarianza", varianza)