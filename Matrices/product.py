# product of matrices
matrix1 = [
    [1, 2],
    [3, 4]
]
matrix2 = [
    [5, 6],
    [7, 8]
]
result = [
    [0, 0],
    [0, 0]
]

for i in range(2):  
    for j in range(2): 
        for k in range(2):  
            result[i][j] += matrix1[i][k] * matrix2[k][j]

print("Product of matrices:")
for row in result:
    print(row)
