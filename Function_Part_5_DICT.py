dict_data_people = {'name' : "Pavel" , "age" : "38", "gender" : "male", "height" : "200", "weight" : "70"}

print(dict_data_people)


for el in dict_data_people:
    print(f'Your {el}:', dict_data_people[el])
    
print()
print ('Добавляем новый элемент:')
dict_data_people['foot'] = 42
print ('новый словарь:', dict_data_people)


print()
print('Удаляем возраст:')
del dict_data_people['age']
print (dict_data_people)