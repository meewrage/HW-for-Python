# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. Пользователь в первой строке вводит натуральное число N – 
#количество элементов в массиве. В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X.

# *Пример:*

# 5
#     7 -2 3 5 1
#     3
#     -> 1
from random import *
N = int(input("Введите длину массива: "))
list = sample(range(-10, 11), N)
print(list)
x = int(input("Введите число от -10 до 10: "))
count = 0
for i in range(len(list)):
    if i == x:
        count += 1
if count != 0:
    print(count)
else:
    print("Нет такого числа")
      