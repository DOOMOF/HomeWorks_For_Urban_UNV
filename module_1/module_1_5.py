immutable_tuple = (1, 3, 5, 'Yap', True)
print('immutable_tuple:', immutable_tuple)
# immutable_tuple [0] = 4 изменить данный элемент не возможно, так как кортежи являеться не изменяем объектом.
mutable_list = [1, 5, 3, False, 'name']
mutable_list[3] = True
print('mutable_list:', mutable_list)
