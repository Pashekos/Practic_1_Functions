"""
Реализуйте программу калькулятор. 
На вход подается три значения: первое число, второе число 
и операция( *, /, + или -) . 
На выходе должны получить число, после выполнения операции.
"""

import random

first_number = random.randint(0,100)
second_number = random.randint(0,100)
list_operation =('+', '-', '/', '*')

operation = random.choice(list_operation)

print (first_number)
print (operation)
print (second_number)

def print_operation(first_number, second_number, operation):
    match operation:
        case '+':
            print ('Результат сложения:', first_number + second_number)
        case '-':
            print ('Результат вычитания:', first_number - second_number)
        case '*':
            print ('Результат умножения:', first_number * second_number)
        case '/':
            try:
                print ('Результат деления', first_number / second_number)
            except ZeroDivisionError:
                print ('На ноль делить нельзя!')
            
print_operation(first_number, second_number, operation)