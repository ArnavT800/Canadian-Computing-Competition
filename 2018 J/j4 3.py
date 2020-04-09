n = int(input())
def rotate(matrix):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in reversed(range(len(matrix))):
            row.append(matrix[j][i])
        result.append(row)
    return result
matrix = []
for i in range(n):
    row = list(map(int, input().split(" ")))
    matrix.append(row)

ltr = False
ttb = False
while not ltr and not ttb:
    if matrix[0][0] < matrix[0][1] and matrix[0][0] < matrix[1][0]:
        ltr = True
        ttb = True
        break
    else:
        matrix = rotate(matrix)
for i in matrix:
    print(*i)


#[[4,3,1], [6,5,2], [9,7,3]]
