
def custom_write(file_name, string):
    string_position = {}
    file = open(file_name, 'a', encoding='utf-8')

    for i, k in enumerate(string):
        i = i + 1
        byte = (i, file.tell())
        string_position[byte] = k
        file.write(f'{k}\n')
    file.close()
    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('text.txt', info)
for elem in result.items():
    print(elem)
