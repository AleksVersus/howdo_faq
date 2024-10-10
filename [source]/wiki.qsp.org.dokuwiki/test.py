import os

curpath = '..\\..\\docs\\wiki\\text_print'
link = '..\\start'

# Вычисление абсолютного пути
absolute_path = os.path.normpath(os.path.join(curpath, link))

print(absolute_path)

print(os.path.splitext(absolute_path))