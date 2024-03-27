'''Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников
в различных компаниях. В первом столбце записано название компании, а во втором — зарплата очередного сотрудника.
Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников и
выводит их названия, каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты,
они должны быть расположены в лексикографическом порядке их названий.'''

import csv

company_dict1 = {}
company_dict2 = {}
company_dict = {}
with open('salary_data.csv', encoding='utf-8')as file:
    rows = csv.reader(file)
    rows_list = list(rows)

    for i in range(len(rows_list)):
        if i > 0:
            value = rows_list[i][0].split(';')
            company_dict1[value[0]] = company_dict1.get(value[0], 0) + int(value[1])
            company_dict2[value[0]] = company_dict2.get(value[0], 0) + 1

    for k1, v1 in company_dict1.items():
        for k2, v2 in company_dict2.items():
            if k1 == k2:
                company_dict[k1] = v1 / v2

    sorted_dict = dict(sorted(company_dict.items(), key=lambda x: (x[1], x[0])))
    for k, v in sorted_dict.items():
        print(k)