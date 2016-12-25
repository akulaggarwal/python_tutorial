def triplets(a, b):
    first = 0
    second = 0
    for i, v in enumerate(a):
        if v > b[i]:
            first+=1
        elif v < b[i]:
            second+=1
    return str(first) + ' ' + str(second)

print(triplets([1, 2, 3], [3, 2, 1]))
