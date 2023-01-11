# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# list = [1, 2, 3, 4, 5]
# print(len(list)//2 + len(list)%2) # целочисленное деление на два. 5// 2 = 2 (без дробной доли 0,5)

# print(len(list)/2) # остаток от деления на два. 5 % 2 = 0.5


# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input('Input a length of random list: '))
result_list = []
list = []

from random import randint
for i in range(n):
    list.append(randint(0, 9))
print(list)

i = 0
while i < len(list)//2 + len(list)%2:
    n = n - 1
    a = list[i] * list[n]
    result_list.append(a)
    i += 1

print(result_list)



