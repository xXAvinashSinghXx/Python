# transpose of the matrices
matrix1 = [
    [1, 2],
    [3, 4]
]
result = [
    [0, 0],
    [0, 0]
]
for i in range(2):
    for j in range(2):
        result[j][i] = matrix1[i][j]

print("Transpose of the Matrix:")
for row in result:
    print(row)
