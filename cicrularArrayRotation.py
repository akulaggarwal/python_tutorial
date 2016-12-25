def circles(n, k, q, arr, m):
    finalArr = [''] * n
    mod = k % n
    for i in range(n):
        newInd = ((mod + i) % n)
        finalArr[newInd] = arr[i]

    for val in m:
        print(finalArr[val - 1])

circles(3, 2, 3, [1, 2, 3], [1, 2, 3])
