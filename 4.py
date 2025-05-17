import os
from random import randint
from datetime import datetime
curr_dir = os.path.dirname(os.path.abspath(__file__))
files = [f for f in os.listdir(curr_dir)]
file = files[randint(0, len(files) - 1)]
file_path = os.path.join(curr_dir, file)
file_size = os.path.getsize(file_path)
created = os.path.getctime(file_path)
modified = os.path.getmtime(file_path)
created = datetime.fromtimestamp(created).strftime('%d.%m.%Y %H:%M:%S')
modified = datetime.fromtimestamp(modified).strftime('%d.%m.%Y %H:%M:%S')
with open('inf.txt', 'w', encoding='utf-8') as f:
    f.write(f'Имя: {file}\n')
    f.write(f'Размер: {file_size} байт\n')
    f.write(f'Дата создания: {created}\n')
    f.write(f'Изменён: {modified}\n')