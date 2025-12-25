""" Задача 1
Используя операции индексирования и разреза, 
вы выводите на экран первый и третий элементы списка [1, 2, 3, 4, 5], 
а также разрезаете список из первых трех элементов.
"""
digit_spisok = [1, 2, 3, 4, 5]
print('Задача #1:')
print('Список до обработки:', digit_spisok)


def elem_spiska(digit_spisok):
    print ('Первый элемент списка:', digit_spisok[0])
    print ('Третий элемент списка:', digit_spisok[2])
    print ('Первые 3 элемента списка:', digit_spisok[0:2])
    print ()
elem_spiska(digit_spisok)    
    
""" Задача 2
Дан список [«Ростов», «+», «на», «-», «Дону»]. 
Исправьте плюс в дефис и введите название города на экране, 
используя доступ к элементам списка по индексам.
"""
spisok_gorod = ['Ростов', '+', 'на', '-', 'Дону']
print('Задача #2:')
print('Список до обработки:', spisok_gorod)

def new_spisok(spisok_gorod):
    spisok_gorod[spisok_gorod.index('+')] = '-'
    print ('Список без знака "+"', spisok_gorod)
    print ('Название города: ', *spisok_gorod, sep='')
    print ()
    
new_spisok(spisok_gorod)

spisok = ["a", "c", "1", "a", "32", "23"]

"""3. Дан список [«а», «с», «1», «а», «32», «23»]. 
Разбейте его на два списка: 
только с буквами и только с цифрами."""

def alpha_digit(spisok):
    print('Задача #3')
    print('Список до обработки:', spisok)
    spisok_digit = []
    spisok_alpha = []
    for i in range (len(spisok)-1, -1, -1):
        if spisok[i].isdigit():
            spisok_digit.append(spisok[i])
        elif spisok[i].isalpha():
            spisok_alpha.append(spisok[i])
    print('Список только из букв:', spisok_alpha)
    print('Список только из цифр:', spisok_digit)
    print()

alpha_digit(spisok)       

         
"""4. В предыдущей задаче необходимо было 
получиться из списка букв. воспользуйтесь 
методами списка: удалите из него
 последний элемент, сделайте реверс списка."""

def del_revers(spisok):
    print('Задача #4')
    print('Список до обработки:', spisok)
    del spisok[-1]
    spisok_revers = spisok[::-1]
    print('Список без последнего элемента:', spisok)
    print('Список в обратном порядке:', spisok_revers)
    print() 

del_revers(spisok)

"""5. Преобразуйте список [«a», «s», «1», «a», «32», «23»] 
в множество и выведите на экран. 
Что изменилось?"""

def transfer_in_set(spisok):
    spisok_new = set(spisok)
    print('Задача #5')
    print('Список до обработки:', spisok)
    print('Список в виде множества:', spisok_new)
    print()

transfer_in_set(spisok)    
    