# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит 
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой 

a = [3, 1, 3, 4, 2, 4, 12]
b = [4, 15, 43, 1, 15, 1]

for i in range(len(a)):
    if a[i] not in b:
        print(a[i], end = ' ')
        

# Решение преподавателя

# Вариант 1.0
count = 0
for i in range(len(first_numbers)):
    for j in range(len(second_numbers)):
        if first_numbers[i] == second_numbers[j]:
            count += 1
    if count != 0:
        print(first_numbers[i])
        
        
# Вариант 1.1
count = 0
for first_num in first_numbers:
    for second_num in second_numbers:
        if first_num == second_num:
            count += 1
    if count != 0:
        print(first_num)
    count = 0
    
    
# Вариант 2.1
print()
print("-" * 20)
for num in first_numbers:
    if num not in second_numbers:
        print(num, end=' ')
        
        
        
        
        
        
        
"""Дан массив, состоящий из целых чисел. Напишите программу, 
которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного. 
Сначала вводится число N — количество элементов в массиве 
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел."""

n = int(input())
list_first = []
for i in range(n):
    num = int(input())
    list_first.append(num)

count = 0
for i in range(1, n - 1):
    if list_first[i - 1] < list_first[i] > list_first[i + 1]:
        count += 1
print(count)


"""43. Дан список чисел. Посчитайте, сколько в нем пар элементов, 
равных друг другу. Считается, что любые два элемента, 
равные друг другу образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках."""

numbers = [1, 2, 3, 2, 2, 2, 3]
# Вариант 1
count = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            count += 1
print(count)



"""Два различных натуральных числа n и m называются дружественными, 
если сумма делителей числа n (включая 1, но исключая само n) равна 
числу m и наоборот. Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, 
каждое из которых не превосходит k. Программа получает на вход 
одно натуральное число k, не превосходящее 105. 
Программа должна вывести  все пары дружественных чисел, 
каждое из которых не превосходит k. Пары необходимо выводить 
по одной в строке, разделяя пробелами. Каждая пара должна быть 
выведена только один раз (перестановка чисел новую пару не дает)."""

k = int(input("Число k = "))
numbers_div = []
for i in range(k):
    summa = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summa += j
    numbers_div.append(tuple([i, summa]))

print(numbers_div)

for i in range(len(numbers_div)):
    for j in range(i, len(numbers_div)):
        if i != j and numbers_div[i][0] == numbers_div[j][1] and numbers_div[i][1] == numbers_div[j][0]:
            print(*numbers_div[i])