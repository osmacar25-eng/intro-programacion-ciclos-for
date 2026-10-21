"""
Ejercicio 2. Total de una progresion aritmetica

"""

A = int(input("ingrese el primer termino A, entre -100 y 100"))
D = int(input("ingrese la diferencia D, entre -100 y 100"))
N = int(input("ingrese la cantidad de terminos de una progresion,entre 0 y 1000"))

suma_total = 0

t = A
for k in range(1, N + 1):
    suma_total = suma_total + t
    t = t + D

print("Suma:", suma_total)
