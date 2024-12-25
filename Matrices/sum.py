# sum of matrices
matrix1 = [
    [1,2],
    [3,4]
]
matrix2 = [
    [5,6],
    [7,8]
]
result = [
    [0,0],
    [0,0]
]
for i in range(2):
    for j in range(2):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("sum of matrices:")
for row in result:
    print(row)  
