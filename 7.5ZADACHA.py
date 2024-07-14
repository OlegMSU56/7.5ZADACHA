import time
import os

directory = r'.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join('.')
        filetime = os.path.getmtime('.')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize('.')
        parent_dir = os.path.dirname('.')
        print(
            f'Обнаружен файл: {file}, '
            f'Путь: {filepath}, '
            f'Размер: {file_size} байт, '
            f'Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')
