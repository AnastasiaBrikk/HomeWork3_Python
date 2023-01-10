# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Input a number: '))

print(bin(n) [2:]) #используется оператор по переводу в двоичную систему счисления. Чтобы убрать префикс берём срез. 
# Можно обойтись и без него:
# list = []
# while n > 0:
#     list.append(n%2)
#     n //=2
# print(list)