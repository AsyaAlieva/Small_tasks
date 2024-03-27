'''Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS,
далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS,
и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.

Напишите программу создания файла answer.txt и вывода в него списка козлов,
которые удовлетворяют условию загадки от Жака Фреско.'''


with open('answer.txt', 'w') as answer_file:
    with open('goats.txt', 'r') as input_file:
        general_list = input_file.readlines()
        goats_list = []

        for word in range(1, len(general_list)):
            count_types = 0

            if general_list[word].rstrip() != 'GOATS':
                goats_list.append(general_list[word])
                count_types += 1
            elif general_list[word].rstrip() == 'GOATS':
                break

        itog_list = dict()
        for word in range(2+len(goats_list), len(general_list)):
            k = 0
            for i in range(2+len(goats_list), len(general_list)): #сначала первое сравниваем со всеми остальными, а потом второе и т. д.
                if general_list[word].rstrip() == general_list[i].rstrip():
                    k += 1
            itog_list[general_list[word].rstrip()] = k

        count_of_goats = len(general_list) - count_types - 2 #общее кол-во объектов
        procent = 0.07 * count_of_goats #кол-во объектов, удовлетворяющих условию

        for key, value in itog_list.items():
            if value > procent:
                print(key)