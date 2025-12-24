
a = 252
b = 24
c = 38
count = 0

"""1. Дано целое число A. 
Проверить истинность высказывания: 
«Число A является положительным»"""

def test_positive_number(a):
    global count
    count += 1
    print(f'Задача №{count}:')
    print (f"Число A = {a} является положительным:")
    if a > 0:
        return (f'Ответ: {True}')
    else:
        return (f'Ответ: {False}')

print(test_positive_number(a))
print()

"""2. Дано целое число A. 
Проверить истинность высказывания: 
«Число A является нечетным»."""    

def test_odd_number(a):
    global count
    count += 1
    print(f'Задача №{count}:')
    print (f"Число A = {a} является нечетным:")
    if a % 2 == 0:
        return (f'Ответ: {False}')
    else:
        return (f'Ответ: {True}')
    
print(test_odd_number(a))
print()


"""3. Дано целое число A. 
Проверить истинность высказывания: 
«Число A является четным»."""

def test_even_number(a):
    global count
    count += 1
    print(f'Задача №{count}:')
    print (f"Число A = {a} является четным:")
    if a % 2 == 0:
        return (f'Ответ: {True}')
    else:
        return (f'Ответ: {False}')
    
print(test_even_number(a))
print()


"""4. Даны два целых числа: A, B. 
Проверить истинность высказывания: 
«Справедливы неравенства A > 2 и B ≤ 3»."""

def neravenstvo(a, b):
    global count
    count += 1
    print(f'Задача №{count}:')
    print (f"Число A = {a} > 2 и Число В = {b} <= 3?")
    if a > 2 and b < 4:
        return (f'Ответ: {True}')
    else:
        return (f'Ответ: {False}')
    
print(neravenstvo(a, b))
print()


"""5. Даны два целых числа: A, B. 
Проверить истинность высказывания: 
«Справедливы неравенства A ≥ 0 или B < −2»."""

def neravenstvo_5(a, b):
    global count
    count += 1
    print(f'Задача №{count}:')
    print (f"Число A = {a} ≥ 0 или Число В = {b} < -2 ?")
    if a >= 0 or b < -2:
        return (f'Ответ: {True}')
    else:
        return (f'Ответ: {False}')
    
print(neravenstvo_5(a, b))
print()

"""6. Даны три целых числа: A, B, C. 
Проверить истинность высказывания:
«Справедливо двойное неравенство A < B < C»."""


def neravenstvo_6(a, b, c):
    global count
    count += 1
    print(f'Задача №{count}:')
    print (f"Число A = {a}, Число В = {b}, Число C = {c}")
    print ('Справедливо двойное неравенство A < B < C?')
    if a < b < c:
        return (f'Ответ: {True}')
    else:
        return (f'Ответ: {False}')
    
print(neravenstvo_6(a, b, c))
print()

"""7. Даны три целых числа: A, B, C. 
Проверить истинность высказывания: 
«Число B находится между числами A и C»"""

def neravenstvo_7(a, b, c):
    global count
    count += 1
    print(f'Задача №{count}:')
    print (f"Число A = {a}, Число В = {b}, Число C = {c}")
    print ('Число B находится между числами A и C?')
    if a < b < c or c < b < a:
        return (f'Ответ: {True}')
    else:
        return (f'Ответ: {False}')
    
print(neravenstvo_7(a, b, c))
print()


"""8. Даны два целых числа: A, B. 
Проверить истинность высказывания: 
«Каждое из чисел A и B нечетное»."""

def neravenstvo_8(a, b):
    global count
    count += 1
    print(f'Задача №{count}:')
    print (f"Число A = {a}, Число В = {b}")
    print ('Каждое из чисел A и B нечетное?')
    if a % 2 != 0 and b % 2 != 0:
        return (f'Ответ: {True}')
    else:
        return (f'Ответ: {False}')
    
print(neravenstvo_8(a, b))
print()


"""9. Даны два целых числа: A, B. 
Проверить истинность высказывания: 
«Хотя бы одно из чисел A и B нечетное»"""

def neravenstvo_9(a, b):
    global count
    count += 1
    print(f'Задача №{count}:')
    print (f"Число A = {a}, Число В = {b}")
    print ('Хотя бы одно из чисел A и B нечетное?')
    if a % 2 != 0 or b % 2 != 0:
        return (f'Ответ: {True}')
    else:
        return (f'Ответ: {False}')
    
print(neravenstvo_9(a, b))
print()


"""Даны два целых числа: A, B. 
Проверить истинность высказывания: 
«Ровно одно из чисел A и B нечетное»"""

def neravenstvo_10(a, b):
    global count
    count += 1
    print(f'Задача №{count}:')
    print (f"Число A = {a}, Число В = {b}")
    print ('Ровно одно из чисел A и B нечетное?')
    if (a % 2 != 0 and b % 2 == 0) or (a % 2 == 0 and b % 2 != 0):
        return (f'Ответ: {True}')
    else:
        return (f'Ответ: {False}')
    
print(neravenstvo_10(a, b))
print()
