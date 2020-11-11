def nonRecursiveFact(n):
    fact = 1
    while(n != 0):
        fact *= n
        n -= 1
    return fact

def recursiveFact(n):
    if(n == 1):
        return 1
    return n * recursiveFact(n-1)
