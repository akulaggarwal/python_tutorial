# basic if conditional:
x = 10;

if x <= 0:
    x = 0
    print(x)
elif x == 1:
    print('whole in 1')
elif x >= 25:
    print('too perfect')
elif x >= 10 :
    x = 'perfect'
    print('this makes no sense')


#basic for loop:
words = ['cat', 'window', 'defenestrate']

for eaWord in words:
    print (eaWord, len(eaWord))
