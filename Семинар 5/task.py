# """Даны два целых числа A и В. 
# Выведите все числа от A до B включительно, в порядке возрастания, 
# если A < B, или в порядке убывания, если A > B """

# def print_number(a, b):
#     if a == b:
#         return f"{a}"
#     if a > b:
#         return f"{a}, {print_number(a - 1, b)}"
# #     if a < b:
# #         return f"{a}, {print_number(a + 1, b)}"


# # print(print_number(1, 15))
# # print(print_number(10, 30))
# # print(print_number(10, 0))


# """Последовательностью Фибоначчи называется последовательность 
# чисел a0, a1, ..., an, ..., где 
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи"""
# # 1 2 3 5 8 13 21 34 55 89

# # My - FIX ERROR
# def fib_rec(n):
#     if n <= 1:
#         return n
#     else:
#         return fib_rec(n - 1) + fib_rec(n - 2)

# print(fib_rec(10))




# cahce = {}
# # My - Memo
# def fib_rec_cache(n):
#     if n not in cahce:
#         cahce[n] = n if n <= 1 else fib_rec_cache(n - 1) + fib_rec_cache(n - 2)
#     return cahce[n]


# def f(n):
#     if n == 0 or n == 1:
#         return 1
#     return f(n - 1) + f(n - 2)

# n = int(input())
# print(f(n -2 ))  # [0, 1, 1, 2, 3]


"""Хакер Василий получил доступ к классному журналу 
и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: 
все максимальные – на минимальные."""


def zamena(list1):
    max = list1[0]
    min = list1[0]
    for i in list1:
        if max < list1[i]:
            max = list1[i]
        if min > list1[i]:
            min = list1[i]
    for j in list1:
        if max == list1[j]:
            list1[j] = min
a= [1,2,3,5]
print(zamena(a))




# # Вариант 1 - max and min
# list_1 = [2, 2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5]
# max_number = max(list_1)
# min_number = min(list_1)

# for i in range(len(list_1)):
#     if list_1[i] == max_number:
#         list_1[i] = min_number
        
# print(list_1)


# # Вариант 2 - Свой max, min
# list_1 = [2, 2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5]
# min_number, max_number = float('inf'), float('-inf')

# for num in list_1:
#     if num > max_number:
#         max_number = num
#     elif num < min_number:
#         min_number = num
        
# print(f'Т - {min_number}, И - {max_number}')

# for i in range(len(list_1)):
#     if list_1[i] == max_number:
#         list_1[i] = min_number
# print(list_1)






list_1 = [2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5]


def return_max_min(numbers):
    min_number, max_number = float('inf'), float('-inf')
    for num in numbers:
        if num > max_number:
            max_number = num
        elif num < min_number:
            min_number = num
    return min_number, max_number

# min_number, max_number = return_max_min(list_1)
# print(f'Т - {min_number}, И - {max_number}')

def replace_max_to_min(numbers):
    min_number, max_number = return_max_min(numbers)
    print(f'Т - {min_number}, И - {max_number}')
    
    for i, num in enumerate(numbers):
        if num == max_number:
            numbers[i] = min_number