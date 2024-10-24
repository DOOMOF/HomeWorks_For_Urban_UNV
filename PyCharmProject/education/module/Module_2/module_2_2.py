first = int(input('введите первое сравниваемое число:'))
second = int(input('введите второе сравниваемое число:'))
third = int(input('введите третье сравниваемое число:'))

print('Сравниваемые числа:', first, second, third)

count = 0

if (first == second and first == third):
    count += 3
elif (first == second or first == third or second == third):
    count += 2
else:
    count = 0
print('Совпадений:', count)
