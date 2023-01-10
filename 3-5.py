# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input('Input a number: '))
            
def Fibonacci(n):
    fib1 = 1
    fib2 = 1
    list = []
    for i in range(n):
        list.append(fib1)
        fib1, fib2 = fib2, (fib1 + fib2)
        
    fib1 = 0
    fib2 = 1
    for j in range(n+1):
        list.insert(0, fib1)
        fib1, fib2 = fib2, fib1 - fib2
    return list
print(Fibonacci(k))