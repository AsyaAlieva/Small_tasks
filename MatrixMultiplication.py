#умножение двух матриц

n, m = map(int, input().split())
matrix_1 = []
for _ in range(n):
    temp = input().split()
    matrix_1.append(temp)
s = input()
m, k = map(int, input().split())
matrix_2 = []
for _ in range(m):
    temp = input().split()
    matrix_2.append(temp)

matrix = []
for _ in range(n):
    matrix.append([0]*k)

counter = 0
for i in range(n): #берем строку из первой матрицы
    for j in range(k): #берем столбец из второй матрицы
        for x in range(m): #нужен чтобы все элементы из строки из 1-ой матрицы умножить на все элементы столбца 2-ой матрицы
            counter = int(matrix_1[i][x]) * int(matrix_2[x][j]) #умножаем элемент из x-ого столбца 1-ой матрицы на элемент из x-ой строки 2-ой матрицы
            matrix[i][j] += counter #суммируем каждое произведение

for el in range(n):
    print(*(matrix[el]))