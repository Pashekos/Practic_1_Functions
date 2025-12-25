import random
no_sorted_list = list(range(1, 32))
random.shuffle(no_sorted_list)

def get_sorted_list(no_sorted_list):
    for j in range(len(no_sorted_list)): #проверяем каждый элемент
        flag = True #ставим флаг, чтобы лишний раз цикл не проходить
        for i in range(len(no_sorted_list)-j-1):#проверяем с каждым элементом кроме передвинутых ранее(ставим "-1" так как i+1 не попадет в диапазон)
            if no_sorted_list[i] > no_sorted_list[i+1]:
                no_sorted_list[i], no_sorted_list[i+1] = no_sorted_list[i+1], no_sorted_list[i]
                flag = False
        if flag:
            break #завершаем, если не было обмена
    return no_sorted_list

print("Первоначальный список:")
print(no_sorted_list)
print("Новый список:")
print(get_sorted_list(no_sorted_list))