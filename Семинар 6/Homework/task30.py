# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Введите первый элемент: "))
b = int(input("Введите разность: "))
c = int(input("Введите количество элементов: "))
d = []
d.append(a)
for i in range(1,c):
    d.append(d[i-1] + b)
print(d)