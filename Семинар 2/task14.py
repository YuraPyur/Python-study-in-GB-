# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите N: "))
i = 1
j=0
while i<=N:  
    print(f"2 в степени {j} равно {i}")
    i = i*2
    j+=1
    