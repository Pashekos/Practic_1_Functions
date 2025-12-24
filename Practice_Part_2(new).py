# Practic_1_Part_2

a = 350
b = 3253
c = 12560
count = 0


""" 1. Дано расстояние L в сантиметрах. 
Используя операцию деления нацело, 
найти количество полных метров в нем
(1 метр = 100 см)"""

def transfer_to_full_metr(a):
    global count
    count +=1
    full_metter = str(a //100)
    print (f'Задача #{count}:')
    print (f'Расстояние: {a}см')
    print ('Количество полных метров =', full_metter)
    print ()

transfer_to_full_metr(a)

    

""" 2. Дана масса M в килограммах.
Используя операцию деления нацело, 
найти количество полных тонн
в ней (1 тонна = 1000 кг)."""

def transfer_to_full_tonn(a):
    global count
    count +=1
    massa = (a // 1000)
    print (f'Задача #{count}:')
    print (f'Общая масса: {a}кг')
    print ('Количество полных тонн =', massa)
    print ()

transfer_to_full_tonn(b)


""" 3. Дан размер файла в байтах. 
Используя операцию деления нацело, 
найти количество полных килобайтов, 
которые занимает данный файл (1 килобайт = 1024 байта)."""

def transfer_to_full_kbytes(a):
    global count
    count +=1
    print (f'Задача #{count}:')
    result = a // 1024
    print (f'Исходный размер в байтах: {a}')
    print ('Количество полных килобайт =', result)
    print ()
    
transfer_to_full_kbytes(c)


""" 4. Даны целые положительные числа A и B (A > B). 
На отрезке длины A размещено максимально возможное 
количество отрезков длины B (без наложений).
Используя операцию деления нацело, 
найти количество отрезков B, размещенных на отрезке A."""

def find_parts_in_length(a, b):
    if a < b:
        a, b = b, a
    result = a // b
    global count
    count +=1
    print (f'Задача #{count}:')
    print (f'Самый длинный отрезок: {a}')
    print ('На нем поместилось коротких отрезков =', result)
    print ()

find_parts_in_length(a,b)


""" 5. Даны целые положительные числа A и B (A > B). 
На отрезке длины A размещено максимально возможное 
количество отрезков длины B (без наложений). 
Используя операцию взятия остатка от деления нацело, 
найти длину незанятой части отрезка A."""

def find_remaining_part (a,b):
    if a < b:
        a, b = b, a
    global count
    count +=1
    print (f'Задача #{count}:')
    result = a % b
    print (f'Общий отрезок: {a}')
    print ('Свободный участок без малых отрезков =', result)
    print ()
    
find_remaining_part(a,b)

""" 6. Дано двузначное число. Вывести вначале его левую цифру 
(десятки), а затем — его правую цифру (единицы). 
Для нахождения десятков использовать операцию деления нацело, 
для нахождения единиц — операцию взятия остатка от деления."""

def find_tens_units(a):
    if a > 99:
        a = a // 10
    tens = (a // 10)
    units = (a % 10)
    global count
    count +=1
    print (f'Задача #{count}:')
    print (f'Дано число: {a}')
    print ('Его десятки =', tens)
    print ('Его единицы =', units)
    print ()

find_tens_units(a)


""" 7. Дано двузначное число. 
Найти сумму и произведение его цифр."""

def find_sum_and_product(a):
    if a > 99:
        a = a // 10
    tens = (a // 10)
    units = (a % 10)
    global count
    count +=1
    print (f'Задача #{count}:')
    print (f'Дано число: {a}')
    print ('Сумма его цифр =', tens + units)
    print ('Произведение его цифр =', tens * units)
    print ()

find_sum_and_product(a)


""" 8. Дано двузначное число. Вывести число, 
полученное при перестановке цифр исходного числа."""
def find_replace_numbers(a):
    if a > 99:
        a = a // 10
    tens = str(a // 10)
    units = str (a % 10)
    result = int (units + tens)
    global count
    count +=1
    print (f'Задача #{count}:')
    print (f'Дано число: {a}')
    print (f'Число после перестановки = {units}{tens}')
    print ()

find_replace_numbers(a)


""" 9. Дано трехзначное число. Используя одну операцию 
деления нацело, вывести первую цифру данного числа (сотни)."""
def find_first_num(a):
    result = a // 100
    global count
    count +=1
    print (f'Задача #{count}:')
    print (f'Дано число: {a}')
    print ('Количество сотен =', result)
    print ()

find_first_num(a)


""" 10. Дано трехзначное число. Вывести вначале его последнюю 
цифру (единицы), а затем — его среднюю цифру (десятки)."""
def find_last_and_midle_num(a):
    units = (a % 10)
    tens = (a // 10 % 10)
    global count
    count +=1
    print (f'Задача #{count}:')
    print (f'Дано число: {a}')
    print ('Последняя цифра данного числа =', units)
    print ('Средняя цифра данного числа =', tens)
    print ()

find_last_and_midle_num(a)