def get_count_positive_numbers(a, b, c):
    count = 0
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1
    logging.debug(f"Count after scan = {count}")
    return count


def find_the_bigger_num(a,  b):
    logging.debug(f"Have got two numbers for check the biggest: {a} and {b}")
    if a > b:
        logging.debug(f"Return the biggest: {a}")
        return a
    else:
        logging.debug(f"Return the biggest: {b}")
        return b    


def sort_the_bigger_and_smaller_nums(a, b):
    if a > b:
        logging.debug(f"Return the biggest and smaller: {a} and {b}")
        return a, b
    else:
        logging.debug(f"Return the biggest and smaller: {b} and {a}")
        return b, a    


def find_the_smaller_num(a, b, c):
    list_numbers = (a, b, c)
    smaller = min(list_numbers)
    logging.debug(f"Return the smaller: {smaller}")
    return smaller


def find_coordinate_quarter(a, b):
    if a > 0 and b > 0:
        logging.debug(f"The coordinate_quarter {a} and {b} = I")
        return "I quarter"
    elif a > 0 and b < 0:
        logging.debug(f"The coordinate_quarter {a} and {b} = II")
        return "II quarter"
    elif a < 0 and b < 0:
        logging.debug(f"The coordinate_quarter {a} and {b} = III")
        return "III quarter"
    elif a < 0 and b > 0:
        logging.debug(f"The coordinate_quarter {a} and {b} = IV")
        return "IV quarter"



import logging 

logging.basicConfig(level=logging.DEBUG, filename="Part_4_log.py",filemode="w", format="%(asctime)1s %(levelname)1s %(message)1s")
logging.debug("Start programm")


first_number = int(input("Введите первое число"))
logging.debug(f"Pushed first_number {first_number}")
second_number = int(input("Введите второе число"))
logging.debug(f"Pushed second_number {second_number}")
third_number = int(input("Введите третье число"))
logging.debug(f"Pushed third_number {third_number}")

#Даны три целых числа.
#Найти количество положительных чисел в исходном наборе.

logging.debug("Go to function get_count_positive_numbers(a, b, c)")
print ("Count the positive numbers = ", get_count_positive_numbers(first_number, second_number, third_number))


#Даны два числа. Вывести большее из них.
logging.debug("Go to function find_the_bigger_num(a, b)")
print('The bigger number:', find_the_bigger_num(first_number, second_number))


#Даны два числа. Вывести вначале большее, а затем меньшее из них.
logging.debug("Go to function sort_the_bigger_and_smaller_nums(a, b)")
print('The bigger number and smaller number:', sort_the_bigger_and_smaller_nums(first_number, second_number))


#Даны три числа. Найти наименьшее из них.
logging.debug("Go to function find_the_smaller_num(a, b, c)")
print('The smaller number:', find_the_smaller_num(first_number, second_number, third_number))

#Даны координаты точки, не лежащей на координатных осях OX и OY. 
#Определить номер координатной четверти, в которой находится данная точка. 
#Координаты задаются пользователем, например (10, 15).
logging.debug("Go to function find_coordinate_quarter(a, b)")
print('The coordinate qyarter:', find_coordinate_quarter(first_number, second_number))
