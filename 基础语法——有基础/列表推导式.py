# 写一个列表推导式，生成一个5*10的矩阵，矩阵内的所有值为1，再写一个列表推导式，把这个矩阵转置
matrix = [[1 for _ in range(10)] for _ in range(5)]

transposed_matrix = [[matrix[j][i] for j in range(5)] for i in range(10)]

print(matrix)
print(transposed_matrix)