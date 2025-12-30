import random

"""Дано целое число K. Вывести строку-описание оценки, 
соответствующей числу K 
1 — «плохо», 
2 — «неудовлетворительно», 
3 — «удовлетворительно», 
4 — «хорошо», 
5 — «отлично»
Если K не лежит в диапазоне 1–5, то вывести строку «ошибка»."""


mark = random.randint(1, 7)
print(mark)

def return_description(mark):
    match mark:
        case 1:
            return("1-плохо")
        case 2:
            return("2-неудовлетворительно")
        case 3:
            return("3-удовлетворительно")
        case 4:
            return("4-хорошо")
        case 5:
            return("5-отлично")
        case _:
            return("ошибка")

#print(return_description(mark))

def return_description_hash_table(mark):
    hash_table = {
        1 : "плохо",
        2 : "неудовлетворительно",
        3 : "удовлетворительно",
        4 : "хорошо",
        5 : "отлично"
    }
    if mark in hash_table:
        return hash_table[mark]
    else:
        return("Ошибка")

print(return_description_hash_table(mark))
print()

"""Дан номер месяца — целое число в диапазоне 1–12 
(1 — январь, 2 — февраль и т. д.). 
Определить количество дней в этом месяце для невисокосного года."""

def return_days_of_month(mark):
    match mark:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12 :
            return("В данном месяце - 31 день")
        case 2:
            return("В феврале - 28 дней")
        case 4 | 6 | 9| 11 :
            return("В данном месяце - 30 дней")
        case _:
            return("ошибка")

print(mark)
print(return_days_of_month(mark))
print()

"""Даны два целых числа: D (день) и M (месяц), 
определяющие правильную дату невисокосного года. 
Вывести значения D и M для даты, следующей за указанной."""

day = random.randint(1, 32)
month = random.randint(1, 13)

def return_next_day_month(day, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if day > days_in_month[month-1] :
        return ("Неверная дата")
    elif day == days_in_month[month-1] :
        day = 1
        if month == 12:
            month = 1
        else:
            month +=1
    else:
        day += 1
    return(day, month)

print("День", day)
print("Месяц", month)
print("Следующая дата:", return_next_day_month(day, month))
print()

"""Робот может перемещаться в четырех направлениях 
(«С» — север, «З» — запад, «Ю» — юг, «В» — восток) и принимать три цифровые команды: 
0 — продолжать движение, 1 — поворот налево, −1 — поворот направо. 
Дан символ C — исходное направление робота и целое число N — посланная ему команда. 
Вывести направление робота после выполнения полученной команды."""


def return_next_day_month_case(day, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > days_in_month[month-1] :
        return ("Неверная дата")
    
    match day:
        case 28 | 30 | 31:
            day = 1
            if month == 12:
                month = 1
            else:
                month +=1
        case _:
            day += 1
    return(day, month)

print("День", day)
print("Месяц", month)
print("Следующая дата:", return_next_day_month_case(day, month))
print()


"""
Робот может перемещаться в четырех направлениях 
(«С» — север, «З» — запад, «Ю» — юг, «В» — восток)
 и принимать три цифровые команды:
 0 — продолжать движение,
 1 — поворот налево,
 −1 — поворот направо.
 Дан символ C — исходное направление робота
 и целое число N — посланная ему команда. 
Вывести направление робота после выполнения полученной команды.
"""

import random 

command = random.randint(-1, 1)

def push_the_direction(command):
    match command:
        case 1:
            return ("Turn the left")
        case -1 :
            return ("Turn the right")
        case 0:
            return ("Go straight")
        case _:
            return ("Wrong direction")
            

print (command)
print (push_the_direction(command))

"""
Дано целое число в диапазоне 100–999. 
Вывести строку-описание данного числа, например: 
256 — «двести пятьдесят шесть», 
814 — «восемьсот четырнадцать».
"""

int_number = random.randint(100, 999)

def print_full_number (int_number):
    hundreds_dict = (
        '',
        'сто',
        'двести',
        'триста',
        'четыреста',
        'пятьсот',
        'шемтьсот',
        'семьсот',
        'восемьсот',
        'девятьсот'
    )
        
    tens_dict = {
        
        1: 'десять',
        2: 'двадцать',
        3: 'тридцать',
        4: 'сорок',
        5: 'пятьдесят',
        6: 'шестьдесят',
        7: 'семьдесят',
        8: 'восемьдесят',
        9: 'девяносто'
        }
    
    units_dict = {
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восемь',
        9: 'девять',
        11: 'одиннадцать',
        12: 'двенадцать',
        13: 'тринадцать',
        14: 'четырнадцать',
        15: 'пятнадцать',
        16: 'шестнадцать',
        17: 'семнадцать',
        18: 'восемнадцать',
        19: 'девятнадцать'
        }
            
    
    hundreds = int_number // 100
    tens = int_number % 100 // 10
    teenage = int_number % 100
    units = int_number % 10
    
    if 10 < (teenage) < 20:
        return (hundreds_dict[hundreds], units_dict[teenage])
    
    elif tens == 0 and units != 0:
        return (hundreds_dict[hundreds], units_dict[units])
 
    elif units == 0 and tens != 0:
        return (hundreds_dict[hundreds], tens_dict[tens])
    
    elif tens == 0 and units ==0 :
        return (hundreds_dict[hundreds])
 
    return (hundreds_dict[hundreds], tens_dict[tens], units_dict[units])
 
print (int_number)
print (*print_full_number(int_number))



"""
Реализуйте программу калькулятор. 
На вход подается три значения: первое число, второе число 
и операция( *, /, + или -) . 
На выходе должны получить число, после выполнения операции.
"""