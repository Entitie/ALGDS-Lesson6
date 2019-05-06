# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# number = input('Введите трёхзначное число: ')

# print(f'Сумма цифр числа равна: {int(number[0]) + int(number[1]) + int(number[2])}')
# print(f'Произведение цифр числа равна: {int(number[0]) * int(number[1]) * int(number[2])}')

#  Давайте проверим, что лучше работа с текстом, цифрами, в цикле for или без. Какой метод лучше?

import timeit

def str_numbers():
    K = '123456789'
    sum_K = int(K[0]) + int(K[1]) + int(K[2]) + int(K[3]) + int(K[4]) + int(K[5]) + int(K[6]) + int(K[7]) + int(K[8])
    # return sum_K


# print(str_numbers())

def str_for_numbers():
    K = '123456789'
    sum_K = 0
    for el in K:
        sum_K += int(el)
    # return sum_K


# print(str_for_numbers())

def int_numbers():
    K = '123456789'
    K = int(K)
    sum_K = K // 100000000 + K // 10000000 % 10 + K // 1000000 % 10 + K // 100000 % 10 + \
            K // 10000 % 10 + K // 1000 % 10 + K // 100 % 10 + K // 10 % 10 + K % 10
    # return sum_K


# print(int_numbers())

def int_for_numbers():
    K = '123456789'
    K = int(K)
    sum_K = 0
    for el in range(9):
        sum_K += K % 10
        K //= 10
    # return sum_K


# print(int_for_numbers())

print(timeit.timeit('str_numbers()', setup='from __main__ import str_numbers', number=100000))
print(timeit.timeit('str_for_numbers()', setup='from __main__ import str_for_numbers', number=100000))
print(timeit.timeit('int_numbers()', setup='from __main__ import int_numbers', number=100000))
print(timeit.timeit('int_for_numbers()', setup='from __main__ import int_for_numbers', number=100000))
