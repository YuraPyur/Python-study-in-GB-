# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# stroka = 'a a a b c a a d c d d'
# stroka = stroka.split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1
    
    


# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


# a = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"      

# a = a.lower().split(' ')
# b = set(a)
# print(len(b))


# # Вариант 1 
# text = """She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells""".split()
# unique_words = set()
# for word in text:
#     unique_words.add(word.lower())
# print(len(unique_words))


# # Вариант 2
# print(len(set(text.lower().split())))



# Ваня и Петя поспорили, кто быстрее решит 
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не 
# такими смышлеными. Никто из ребят не смог до 
# конца сделать это задание. Они решили так: у кого 
# будет меньше ошибок в коде, тот и выиграл спор. За 
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих 
# слайдах


# a = [1, 2, 3, 0, 1, 4, 6, 0, 1, 2]
# MAX = 0
# max = 0
# i = 0
# while i < len(a):
#     if a[i] > max and a[i]!=0:
#         max = a[i]
#         i+=1
#     else:
#         MAX = max
#         i+=1
# if MAX > max:
#     print(MAX)
# else:
#     print(max)


# решение преподавателя

# n = int(input())
# max_number = n
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)