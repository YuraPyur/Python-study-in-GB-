# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input("Введите число : "))
b = int(input("Введите степень: "))

def vosv_v_stepen(x,y):    
    if y == 0:
        return 1
    else:
        return x*(vosv_v_stepen(x, y - 1))     
print(vosv_v_stepen(a,b))
        