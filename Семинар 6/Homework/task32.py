# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# После загрузки задания, вы можете проверить себя самостоятельно с помощью эталонного решения

a = int(input("Введите минимальный элемент диапозона: "))
b = int(input("Введите максимальный элемент диапозона: "))
c = int(input("Введите количество элементов массива: "))
d = []
e = []
for i in range(c):
    d.append(int(input("Введите значение элемента массива: ")))
    if d[i] >= a and d[i] <= b:
        e.append(i)

print("Индексы элементов массива, которые входят в заданный диапозон: ", *e)