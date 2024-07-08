# module_2_5.py Домашняя работа по уроку "Функции в Python.Функция с параметром"
def get_matrix(n, m, value):
    matrix = []
    for a in range(0, n):
        matrix.append([])
        for b in range(0, m):
            matrix[a].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
