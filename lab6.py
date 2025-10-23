import os
import math
import time
import shutil
from functools import reduce
t = input().split()
t = [float(x) for x in t]
p = reduce(lambda a, b: a * b, t)
print(f"{p}") 

t1 = input()
ambal= sum(1 for c in t1 if c.isupper())
gnom= sum(1 for c in t1 if c.islower())
print(f"амбалы: {ambal}, гоблины: {gnom}")

t2 = input()
cleaned = ''.join(c.lower() for c in t2 if c.isalnum())
print("da" if cleaned == cleaned[::-1] else "net")

t3 = float(input())
delay = int(input( ))
time.sleep(delay / 1000)
print(f"{n} после {delay} мс = {math.sqrt(n)}")

t4 = tuple(input().split())
converted = [x.lower() == "true" or x == "1" for x in t4]
print(all(converted))

path = input()
print("Папки:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Файлы:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

path1 = input()
print("Существует:", os.path.exists(path1))
print("Читается:", os.access(path1, os.R_OK))
print("Пишется:", os.access(path1, os.W_OK))
print("Исполняется:", os.access(path1, os.X_OK))



path2 = input("Укажи путь: ")
if os.path.exists(path2):
    print("Путь существует")
    print("Папка:", os.path.dirname(path2))
    print("Файл:", os.path.basename(path2))
else:
    print("Путь не существует")


path3 = input()
with open(path3, 'r', encoding='utf-8') as f:
    print("Количество строк:", sum(1 for _ in f))


lst = input().split()
path4 = input("имя : ")
with open(path4, 'w', encoding='utf-8') as f:
    for item in lst:
        f.write(item + '\n')
print("записан")


for i in range(65, 91):
    with open(f"{chr(i)}.txt", 'w') as f:
        f.write(f"Файл {chr(i)}.txt создан.\n")
print("созданы")


src = input("Источник: ")
dst = input("Назначение: ")
shutil.copyfile(src, dst)
print("скопирован")


path5 = input()
if os.path.exists(path5):
    if os.access(path5, os.W_OK):
        os.remove(path5)
        print("удалён")
    else:
        print("Нет прав")
else:
    print("дурак что ли")

