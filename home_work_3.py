# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# list = [2, 3, 5, 9, 3, 6]
# i = 1
# sum = 0
# while i < len(list):
#     sum += list[i]
#     i += 2
# print(sum)
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# import math

# list = [2, 3, 4, 5, 6]
# list1 = []
# for i in range(math.ceil(len(list)/2)):
#     list1.append(list[i]*list[-1-i])
# print(list1)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# list = [1.1, 1.2, 3.1, 10.01, 5]
# list1 = []
# for i in list:
#     if i%1 != 0:
#         list1.append(round(i % 1, 2))
# max = min = list1[0]
# for i in list1:
#     if max < i:
#         max = i
#     elif min > i:
#         min = i

# print(max-min)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
N = int(input('Введите число: '))
list = []
# def bin_num(N):
#     if N == 0: return 1
#     list.append(N%2)
#     bin_num(N//2)
# bin_num(N)
# list.reverse()
# print(*list)
# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    if n >= 0:
        if n == 0:
            return 0
        elif n in [1, 2]:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    else:
        if n == -1:
            return 1
        elif n == -2:
            return -1
        else:
            return fib(n+2)-fib(n+1)


for i in range(-N,N+1):
    list.append(fib(i))
print(list)
# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
