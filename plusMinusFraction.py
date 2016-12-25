def frac(input):
    pos = 0
    neg = 0
    zero = 0
    for v in input:
        if v < 0:
            neg+=1
        elif v == False:
            zero+=1
        else:
            pos+=1
        l = len(input)
    return str(round(pos/l, 5)) + str(round(neg/l, 5)) + str(round(zero/l, 5))

print(frac([5, 3, -1, -1, 3, 0]))
