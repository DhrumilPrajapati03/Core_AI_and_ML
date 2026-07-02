def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    raws = len(a)
    cols = len(a[0])

    result = [[0 for i in range(raws)] for i in range(cols)]

    for i in range(raws):
        for j in range(cols):
            result[j][i] = a[i][j]

    return result   
print(transpose_matrix([[2,3,6],[9,6,3]]))


# print(result)