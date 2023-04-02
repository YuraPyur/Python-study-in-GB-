"""Вспоминаем функции."""


def get_number_string(num: int) -> str:
    """Функция возвращает строку с числом.

    Args:
        num (int): Число, которое необходимо вывести.

    Returns:
        str: Строка с числом.
    """
    return f"Твоё число {num}"


# Вывод результата
num_string = get_number_string(10)
print(num_string)

# Можно записать и так
# print(get_number_string(11))

# # -----------------------------
# # Будет ли тут ошибка?
# # num_string = get_number_string()

# # А что будет внутри переменной? Будет ошибка?
# what = get_number_string
# print(what)


# # Создадим функцию
# def print_function_string(func: get_number_string) -> None:
#     """Принимает функцию func и передаёт фиксированный аргумент внутрь func.

#     Args:
#         func (get_number_string): Некоторая функция.
#     """
#     print(func(11010))


# print_function_string(what)


"""Анонимные функции (lambda)."""


# Функция, которая возвращает квадрат числа
def square(number: int) -> int:
    return number ** 2


print(square(110))

# Использование Lambda функции
# lambda параметр: результат
square_l = lambda number: number ** 2
print(square_l(11))
print((lambda number: number ** 2)(11))


# --------------------------
# Ещё пример
def return_true() -> bool:
    return True


print(return_true)

return_true_l = lambda: True
print(return_true_l())

# --------------------------
# Вернёмся к 1_function.py -> print_function_string 
# и перепишем её через lambda

# ???




"""Использование встроенного filter. 
Функция filter() принимает два параметра. 
Первый — имя созданной пользователем функции, 
а второй — итерируемый объект 
(список, строка, множество, кортеж и так далее)."""

# filter(функци, последовательность)

numbers = [1, 2, 3, 4, 5, 4, 16, 2, 24]

print(list(filter(lambda number: number >= 3, numbers)))


"""Использование встроенного map."""

numbers = [1, 2, 3, 4, 5, 4, 16, 2, 24]


def preproc_numbers(x):
    if x > 2:
        return str(x)
    else:
        return float(x)

print(list(map(lambda x: str(x) if x > 2 else float(x), numbers)))
print(list(map(preproc_numbers, numbers)))



"""Использованиие sorted."""

# Набор чисел
numbers = [4, 1, 5, 1, 2, 3, 9, 7]
# Сортируем по возрастанию
print(sorted(numbers))
# Сортируем по убыванию
print(sorted(numbers, reverse=True))

# Набор строк
# names = ["Дмитрий", "Алексей", "Елена", "Антон", "Андрей"]
# print(sorted(names))

# # Имя и возраст
# names = [("Дмитрий", 28), ("Алексей", 21), ("Елена", 17), ("Антон", 24), ("Андрей", 23)]
# print(sorted(names))


# Сортировка по возрасту
# def key_age(user: tuple) -> int:
#     return user[1]


# print(sorted(names, key=key_age, reverse=True))

# Используем Lambda



"""Функция zip() в Python создает итератор, который объединяет элементы 
из нескольких источников данных. Эта функция работает со списками, 
кортежами, множествами и словарями для создания списков или кортежей, 
включающих все эти данные."""

employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

zipped_values = zip(employee_names, employee_numbers)
zipped_list = list(zipped_values)

print(zipped_list)

# Вот пример использования zip() для итерации по массивам:
employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

for name, number in zip(employee_names, employee_numbers):
    print(name, number)

# Но как восстановить их прежнюю форму?

employees_zipped = [('Дима', 2), ('Марина', 9),
                    ('Андрей', 18), ('Никита', 28)]
employee_names, employee_numbers = zip(*employees_zipped)

print(employee_names)
print(employee_numbers)