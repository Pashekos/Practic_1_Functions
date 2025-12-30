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