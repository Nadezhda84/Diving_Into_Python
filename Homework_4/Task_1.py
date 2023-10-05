# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def trans_matrix(mat: list) -> list[int]:
    return list(map(list, zip(*mat)))


matrix = [[1, 2, 3], [4, 5, 6]]

new_matrix = trans_matrix(matrix)

print(*matrix, sep='\n')
print()
print(*new_matrix, sep='\n')
