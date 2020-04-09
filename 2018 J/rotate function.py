def rotate(matrix):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in reversed(range(len(matrix))):
            row.append(matrix[j][i])
        result.append(row)
    return result
print(rotate([[4,3,1], [6,5,2], [9,7,3]]))
