def kidnap(mag, ransom):
    magCounter = {}
    for val in mag:
        if (val in magCounter):
            magCounter[val]+=1
        else:
            magCounter[val] = 1

    for val in ransom:
        if (val not in magCounter):
            return "No"
        magCounter[val]-=1

    return 'Yes'

magazine = [ 'give', 'me', 'one', 'one', 'grand', 'today', 'night' ]
ransom = [ 'give', 'one', 'grand', 'today' ]

print(kidnap(magazine, ransom))
