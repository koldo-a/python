# Exercise 1

lista = ['manzana', 'pera', 'fresa', 'piña']
print(lista)

tupla = ('manzana', 'pera', 'fresa', 'piña')
print(tupla)

num1 = float(127/5)
print(num1)

num2 = int(2023/3)
print(num2)

from decimal import Decimal
num3 = Decimal(2023/123)
print(num3)

diccionario = { "frutas" : ['manzana', 'pera', 'fresa', 'piña']}
print(diccionario['frutas'])

# Exercise 2

import math
print(math.ceil(num1))

# Exercise 3

print(math.sqrt(num1))

# Exercise 4

print(diccionario["frutas"][0])


# Exercise 5

print(tupla[0])

# Exercise 6

lista.extend(['sandía'])
print(lista)

# Exercise 7

lista[0] = 'plátano'
print(lista)

# Exercise 8

lista.sort()
print(lista)

# Exercise 9

tupla += ('kiwi',)

fruta1, fruta2, fruta3, fruta4, fruta5 = tupla

print(fruta1)
print(fruta2)
print(fruta3)
print(fruta4)
print(fruta5)