"""
Ejercicio 1. Secuencia entre dos limites

Formula o relacion del profesor:
El paso entre terminos es 1 si A <= B y -1 si A > B.
"""

A = int(input("Ingrese el limite inicial A entre -100 y 100: "))
B = int(input("Ingrese el limite final B entre -100 y 100: "))

if A <= B:
    paso = 1
else:
    paso = -1

for numero in range(A, B + paso, paso):
    print(numero)

