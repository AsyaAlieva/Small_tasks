'''Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса.
В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты.
Напишите программу, которая создает файл domain_usage.csv - где,
в первом столбце записано название почтового домена,
а во втором — количество пользователей, использующих данный домен.
Домены в файле должны быть расположены в порядке возрастания количества их использований,
при совпадении количества использований — в лексикографическом порядке.'''

import csv

with open('data.csv', 'r', encoding='utf-8') as read_file:
    with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as write_file:
        data = csv.reader(read_file)
        data_list = list(data)
        result = {}

        columns = ['domain', 'count']
        for i in range(len(data_list)):
            if i > 0:
                email = data_list[i][2]
                domen = email[email.index('@'):].replace('@', '')
                result[domen] = result.get(domen, 0) + 1 #словарь, где ключи - домены, а значения - сколько пользователей у домена

        dict_list = []
        for key, value in result.items():
            local_dict = {}
            local_dict['domain'] = key
            local_dict['count'] = value
            dict_list.append(local_dict) #засовываем в список словари с ключами domain и count


        def sort_key(item):
            return (item['count'], item['domain'])

        sorted_dict_list = sorted(dict_list, key=sort_key)

        writer = csv.DictWriter(write_file, fieldnames=columns, delimiter=',')
        writer.writeheader()
        writer.writerows(sorted_dict_list)

