# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
n = int(input('Input a length of random list: '))


def FillRandomList(n):
    list1 = []
    from random import randint
    for i in range(n):
        list1.append(randint(0, 9))
    return list1


def proiz(list):      # работает через раз. Непонятно почему
    last_index = len(list)-1
    for i in list:
        if list.index(i) < len(list)/2:
            print(i*list[(last_index-list.index(i))])
        else:
            break

random_list = FillRandomList(n)
print(random_list)
proiz(random_list)
