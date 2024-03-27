'''На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m,
заполнив её "диагоналями" в соответствии с образцом.'''

n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append([0]*m)

k = 1
for i in range(n + m - 1):
    for j in range(max(0, i - m + 1), min(i + 1, n)):
        matrix[j][i - j] = k
        k += 1

for row in matrix:
    print(''.join(str(elem).ljust(3) for elem in row))