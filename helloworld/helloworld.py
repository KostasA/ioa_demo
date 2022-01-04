def mathematics(n):
    return lambda a: a*n

def printList(l):
    for x in l:
        print(x)

x = lambda a : a + 10
y = lambda a,b: a*b


fmath = mathematics(2)

print(fmath(5))

#print(y(10,10))
#l=["A","B","C"]
#printList(l)

