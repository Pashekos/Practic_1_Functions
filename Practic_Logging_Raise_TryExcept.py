def division(a, b):
    if b == 0:
        logging.debug(f"Message from RAISE: FOUND ZERO!{a}, {b}")
        raise ZeroDivisionError(f"Other message from Raise: Division_By_Zero")
    return (a/b)

import logging 

logging.basicConfig(level=logging.DEBUG, filename="py_log.py",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
logging.debug("Start programm")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")

import random

try:
    for num in range(1, 6):
        logging.debug(f"Try to do function #{num}")
        print (f'СООБЩЕНИЕ ИЗ Try: Ответ по делению примера №{num}:', 
        division (random.randint(1, 6), random.randint(0, 1)))
        logging.debug(f"Sucsess function #{num}")

except ZeroDivisionError as el:
    print (el)
    logging.warning (f"DivizinByZero {el}")
    
finally:
    print('СООБЩЕНИЕ ИЗ Fainally: В любом случае программа завершается безаварийно')
    logging.debug("Programm completed")