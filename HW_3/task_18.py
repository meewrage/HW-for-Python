# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. 
# Если таких элементов несколько, вы вывести один любой. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X
# *Пример:*
# 5
#     7 -2 3 5 1
#     6
#     -> 7
from random import *
N = int(input("Введите длину массива: "))
list = sample(range(-10, 11), N)
print(list)
x = int(input("Введите число: "))
res = list[0]
for i in range(len(list)- 1):
    if abs(x - res) >= abs(x - list[i + 1]):
        res = list[i + 1]
print(res)