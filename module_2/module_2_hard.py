print('Введите число от 3 до 20')
numbers = int(input())
list_ = []
for i in range(1, 20):
    if numbers <= 2:
        print('это число не используется')
        break
    for j in range(1, 20):
        if i >= j:
            continue
        else:
            multiple = numbers % (i + j)
            if multiple == 0:
                list_.append([i, j])

print('пары чисел', *list_)