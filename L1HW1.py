# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# number = input('Введите трёхзначное число: ')

# print(f'Сумма цифр числа равна: {int(number[0]) + int(number[1]) + int(number[2])}')
# print(f'Произведение цифр числа равна: {int(number[0]) * int(number[1]) * int(number[2])}')

#  Давайте проверим, что лучше работа с текстом, цифрами, в цикле for или без. Какой метод лучше?

# !!!НОВОЕ!!!
# Python 3.7.3
# System Type   x64-based PC
# Давайте изменим код и не только узнаем какая вариант быстрее, но и какой занимает меньше памяти

import timeit
import sys


def str_numbers():
    K = '123456789'
    sum_K = int(K[0]) + int(K[1]) + int(K[2]) + int(K[3]) + int(K[4]) + int(K[5]) + int(K[6]) + int(K[7]) + int(K[8])
    print(f'K - {sys.getsizeof(K)}')
    print(f'sum_K - {sys.getsizeof(sum_K)}')
    print(f'Всего памяти задействованно - {sys.getsizeof(K) + sys.getsizeof(sum_K)}')
    return sum_K


print(str_numbers())
# print(timeit.timeit('str_numbers()', setup='from __main__ import str_numbers', number=100000))
print()


def str_for_numbers():
    K = '123456789'
    sum_K = 0
    for el in K:
        sum_K += int(el)
    print(f'K - {sys.getsizeof(K)}')
    print(f'sum_K - {sys.getsizeof(sum_K)}')
    print(f'Всего памяти задействованно - {sys.getsizeof(K) + sys.getsizeof(sum_K)}')
    print(f'el - {sys.getsizeof(el)}?')
    return sum_K


print(str_for_numbers())
# print(timeit.timeit('str_for_numbers()', setup='from __main__ import str_for_numbers', number=100000))
print()


def int_numbers():
    K = '123456789'
    K = int(K)
    sum_K = K // 100000000 + K // 10000000 % 10 + K // 1000000 % 10 + K // 100000 % 10 + \
            K // 10000 % 10 + K // 1000 % 10 + K // 100 % 10 + K // 10 % 10 + K % 10
    print(f'K - {sys.getsizeof(K)}')
    print(f'sum_K - {sys.getsizeof(sum_K)}')
    print(f'Всего памяти задействованно - {sys.getsizeof(K) + sys.getsizeof(sum_K)}')
    return sum_K


print(int_numbers())
# print(timeit.timeit('int_numbers()', setup='from __main__ import int_numbers', number=100000))
print()


def int_for_numbers():
    K = '123456789'
    K = int(K)
    sum_K = 0
    for _ in range(9):
        sum_K += K % 10
        K //= 10
    print(f'K - {sys.getsizeof(K)}')
    print(f'sum_K - {sys.getsizeof(sum_K)}')
    print(f'Всего памяти задействованно - {sys.getsizeof(K) + sys.getsizeof(sum_K)}')
    print(f'_ - {sys.getsizeof(_)}?')
    return sum_K


print(int_for_numbers())
# print(timeit.timeit('int_for_numbers()', setup='from __main__ import int_for_numbers', number=100000))
print()

# Получается сумма всегда одинаковая, но как str переменная "более тяжёлая". В последнем варианте K меньше, т.к.
# она преобразуется в процессе выполнения программы, но мы помним, что это самое медленное исполнение кода.
# Отдельно хотелось бы понять, сколько было потрачено памяти дополнительно в ходе выполнения программы через цилкы с
# использованием el, _ и range.
