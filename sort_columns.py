'''Вам доступен файл deniro.csv, каждый столбец которого содержит либо только числа, либо строковые значения.
Напишите программу, которая сортирует содержимое данного файла по указанному столбцу.
Причем данные должны быть отсортированы в порядке возрастания чисел, если столбец содержит числа,
и в лексикографическом порядке слов, если столбец содержит слова.'''

import csv

n = int(input())
with open('deniro.csv') as file:
    data = csv.reader(file)
    sort_data = sorted(data, key=lambda x: int(x[n-1]) if x[n-1].isdigit()==True else x[n-1])

    for i in sort_data:
        print(*i, sep=',')