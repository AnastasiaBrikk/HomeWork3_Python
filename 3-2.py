# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
def proiz(list):
    last_index = len(list)-1
    for i in list:
        if list.index(i) < len(list)/2:
            print(i*(list[last_index]-list.index(i)))
proiz(list1)
proiz(list2)
