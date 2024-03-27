'''Функция должна возвращать словарь, в котором ключом является название столбца файла filename,
а значением — список элементов этого столбца.'''

import csv

def csv_columns(filename):
    with open(filename, encoding='utf-8') as file:
        rows = csv.reader(file)
        list_rows = list(rows)
        n = len(list_rows[0])  # кол-во столбцов в файле (т.е сколько будет ключей)

        my_dict = {}

        for j in range(n):
            lis = []
            for i in range(len(list_rows)):
                if i > 0:
                    a = list_rows[i][j]
                    lis.append(a)
            my_dict[list_rows[0][j].lstrip('\ufeff')] = lis

    return my_dict

filename = input("Введите название csv файла: ")
print(csv_columns(filename))