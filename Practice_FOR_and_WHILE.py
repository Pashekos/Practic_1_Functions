"""
Напишите программу для подсчета среднего числа всех 
введенных пользователем чисел. 
Ввод пользователя должен осуществляться с помощью ввода. 
Если пользователь вводит ноль, то выводиться на экран будет 
среднее значение. 
Использовать цикл while для решения данных задач
"""

import random

count = 0
sum_numbers = 0
i = random.randint(0, 10)

while i > 0:
    input_number = random.randint(0, 10)
    count +=1
    sum_numbers += input_number
    print (input_number)
    i -= 1

if count == 0 or sum_numbers == 0:
    print ('Средняя сумма при 0:', 0)
else:
    print ('Средняя сумма:', sum_numbers / count)


"""
Напишите программу для вывода на экран чисел от 0 до 100.
"""

print ()
print ('Вывести числа от 1 до 100:')
for i in range (101):
    print (i)

"""
Напишите программу для получения таблиц умножения от 0 до 9. 
Используйте вложенный цикл для печати и диапазона.
Пример:
0*1 = 0
0 * 2 = 0
…..
9*1 = 9
9*2=18
"""


print ()
print ('Таблица умножения:')
print ()

for i in range (1, 10):
    for el in range (1, 4):
        if el == 1:
            print (f'{el}*{i}=', i*el, end = '  | ')
        elif el > 1  and el*i < 10:
            print (f'{el}*{i}=', i*el, end = '  | ')
        else:
            print (f'{el}*{i}=', i*el, end = ' | ')
    print()    
    
print ('', '-'*27)
    
for i in range (1, 10):    
    for el in range (4, 7):
        if el > 1  and el*i < 10:
            print (f'{el}*{i}=', i*el, end = '  | ')
        else:
            print (f'{el}*{i}=', i*el, end = ' | ')
    print()    
    
print ('', '-'*27)

for i in range (1, 10):    
    for el in range (7, 10):
        if el > 1  and el*i < 10:
            print (f'{el}*{i}=', i*el, end = '  | ')
        else:
            print (f'{el}*{i}=', i*el, end = ' | ')
    print()        


"""
Составьте список с разными значениями, 
пройдите по нему в цикле и переведите на экран. 
(Сделайте тоже самое со словарем, и вы введете ключ и значение)
"""
print ()

some_list = ['home', 'mouse', 'ten', 'first']
some_dict = {
    1: 'home', 
    2: 'mouse', 
    3: 'ten', 
    4: 'first'
    }
    

    
print ('Print some list:')
print (some_list)
for el in some_list:
    print(el)    
    
    
print()
print ('Print some dict:')
print (some_dict)
for el in some_dict:
    print(el, some_dict[el])        
    