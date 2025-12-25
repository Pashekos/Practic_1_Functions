massiv = list(range(1, 101))
target = int(input('Введите число от 1 до 100:'))

def find_index_target(massiv, target):
    left = 0
    right = len(massiv)-1

    while left <= right: #почему пока равно????
        mid = (left + right) // 2 #находим середину
        if massiv[mid] == target:
            return mid
        elif massiv[mid] > target:
            right = mid - 1 #сдвигаем правую границу
        else:
            left = mid + 1 #сдвигаем левую границу
    return None

print ('Индекс вашего числа:', find_index_target(massiv, target))