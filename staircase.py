def stairs(n):
    for x in range(n):
        n1 = x + 1
        print((n - n1) * ' ' + n1 * '#')

stairs(6)
