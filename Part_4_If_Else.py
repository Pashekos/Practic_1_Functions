def get_count_positive_numbers(a, b, c):
    count = 0
    logging.debug(f"Count = {count}")
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1
    logging.debug(f"Count after scan = {count}")
    return count
    

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
print (get_count_positive_numbers(first_number, second_number, third_number))


#Даны два числа. Вывести большее из них.