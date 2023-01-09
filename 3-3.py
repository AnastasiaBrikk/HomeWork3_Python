# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# float - int = дробная часть

list1 = [2.1, 1.53, 1.1, 5.11, 10.01]
list2 = [1.1, 1.2, 3.1, 5, 10.01]

def GetMaxDif(list):
    max_dif = 0
    min_dif = 1
    for i in list:
        if float(i) - int(i) > max_dif:
            max_dif = round(float(i) - int(i), 2)
        if float(i) - int(i) < min_dif:
            min_dif = round(float(i) - int(i), 2)
    print(max_dif - min_dif)

GetMaxDif(list1)
GetMaxDif(list2) 




