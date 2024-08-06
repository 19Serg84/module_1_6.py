my_dict = {'Vasy': 1989, 'Dima': 1975, 'Vera': 1995}
print(my_dict)
print(my_dict['Vasy'])
print(my_dict.get('Alex', 'ключ не найден'))
my_dict.update({'Nika': 1996, 'Sima': 1979})
print(my_dict)
a = my_dict.pop('Dima')
print(a)
print(my_dict)

print('Ниже работа с множеством')
my_set = {1,2,2,3,3,5.34,5.34,'Den','Den','Eva',True,(1,2,3,5,7)}
print(my_set)
my_set.add(7)
my_set.add('Егор')
my_set.discard(1)
print(my_set)