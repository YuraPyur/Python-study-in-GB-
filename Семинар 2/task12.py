# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input("S = "))
P = int(input("P = "))
x = 1
y = 1
j = 1
for x in range(1001):
    for y in range(1001):
        s = x+y
        p = x*y
        if S==s and P==p:
            print(f"Вариант {j}: Х равен {x}, Y равен {y}")
            j+=1