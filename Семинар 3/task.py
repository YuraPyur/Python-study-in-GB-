# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# a = input("Введите числа ")
# a1 = sorted(a.split())
# j = 1
# for i in range(len(a1)-1):
#     if a1[i] == a1[i+1]:
#         j+=1
# print(j)

# Решение преподавателя

# numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

# # Вариант 2
# result = []
# for num in numbers:
#     if num not in result:
#         result.append(num)
# print(len(result))


# import random


# numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
# numbers = [random.randint(0, 100) for _ in range(10)]



# numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
# for num in numbers:
#     while numbers.count(num) != 1:
#         numbers.remove(num)
# print(numbers)



# print(len(set(numbers)))





# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# a = [1, 2, 3, 4, 5]
# a1 = []
# k = 2
# for i in range(len(a)):
#     a1.append(a[i-k])
# print(a1)


# вариант преподавателя

# for _ in range(k):
#     numbers.insert(0, numbers.pop())
# print(numbers)




# Напишите программу для печати всех уникальных 
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
# ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# list_1 = [{"V": "S001", "V12": "S0012"}, {"V": "S002"}, {"VI": "S001"},
#           {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# # Вариант 1 - original
# unique_kyes = set()
# for value in list_1:
#     for key in value:
#         unique_kyes.add(value[key])
# print(unique_kyes)


# # Вариант 2
# unique_kyes = set()
# for value in list_1:
#     unique_kyes.update(value.values())
# print(unique_kyes)


# d = {'Alex': 21, 'Dima': 25, 'Sveta': 27}
# list_dicts = [{'Alex': 21, 'Dima': 25, 'Sveta': 27}, {'Alex': 'Cv', 'Dima': 'NLP', 'Sveta': "ML"}]
# print(list_dicts[1]['Sveta'], list_dicts[0]['Sveta'])





# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)