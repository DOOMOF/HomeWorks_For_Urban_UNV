my_dict = {'Egor': 2002, 'Roman': 1995, 'Sacha': 2000}
print('dict:', my_dict)
print('Existing value:', my_dict['Roman'])
print('Not existing value:', my_dict.get('Vova'))
my_dict.update({'Andrei': 1999, 'Karen': 1998})
print('Modified dictionary:', my_dict)
a = my_dict.pop('Andrei')
print('Deleted value:', a)

my_set = {"Повидло", 14.36, 4}
print('Set:', my_set)
my_set.update(['Доска', (4, 5)])
print('Update set:', my_set)
my_set.remove(14.36)
print('Deleted:', my_set)
