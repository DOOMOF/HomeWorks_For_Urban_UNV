import os
import time


directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        if os.path.exists(filepath):
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(__file__)
            print(f'Обнаружен файл: {file}, Путь: {__file__}, Размер: {filesize} байт,'
                  f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
