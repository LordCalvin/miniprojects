L = []
def listmaker(n):
    for i in range(n+1):
        if i >= 2:
            L.append(i)
    return L
def Sieve():
    n = 2
    while n <L[-1]:
        for i in L:
            if i != n and i % n == 0:
                L.remove(i)
        n+=1    
    return L
    
listmaker(1000)
print Sieve()
