'''
#basic if conditional:
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
    print (eaWord, 'length:', len(eaWord))

#range
print(range(3))
print(list(range(3)))
shortRange = range(0, 4, 2)

for i in shortRange:
    print(i)


#fibonacci
def fib(n):
    if n <= 1:
        print("n is bad")
        return "n is bad"
    a, b = 1, 1
    result = [b]
    while a < n:
        a, b = b, a + b
        print(a, end='/')
        result.append(a)
    print(result)
    return result

fib(10)


 #Study arguments again: 4.7.3 onwards

 #lambda
def myAdder(n):
    return lambda x: x + n

g = myAdder(3)
h = g(4)
print(h)

###########Ch. 5###########
#Basic list (JS array) methods: 5.1

#Queue
from collections import deque
myQueue = deque(["pears", "trees", "spaceships"])
myQueue.append("death")
myQueue.append('happy')
myQueue.popleft()
print(myQueue)


#list comprehension
x = [x**2 for x in range(5)]
print(x)
y = list(map(lambda x: x**2, range(10)))
print(y)

#tuples: declared without any enclosers, like lists but immutable,
#        for empty: (), for 1: 'val',
#        notice the trailing comma for 1


#sets: use {}, cannot have duplicates


#dictionaries: basically same as JS objects, section 5.5


#9: scope and classes
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam) #"test spam"
    do_nonlocal()
    print("after nonlocal assignment:", spam) #"non-local spam"
    do_global()
    print("After global assignment:", spam) #"non-local spam"

scope_test()
print("In global scope:", spam) #"global spam"
'''

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

class Derived(Complex):
    def somethingItsOwn(self):
        # whatever
#can also do multiple inheritence, via (a, b, c...
#checks a first, then b, then c
