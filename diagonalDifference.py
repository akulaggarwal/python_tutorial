def diff(m):
    l = len(m)
    diag1 = 0
    diag2 = 0
    for i, v in enumerate(m):
        diag1+=v[i]
        diag2+=v[l - 1 - i]
    return abs(diag1 - diag2)

matrix = [[1, 2, 3], [2, 3, 4], [3, 5, 7]]
print(diff(matrix))
