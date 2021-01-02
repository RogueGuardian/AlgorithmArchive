def nonRecursiveFact(n):
    # Returning -1 when n is not valid
    if(n < 0):
        return -1

    fact = 1
    while(n != 0):
        fact *= n
        n -= 1
    return fact

def recursiveFact(n):
    # Returning -1 when n is not valid
    if(n < 0):
        return -1

    if(n == 0):
        return 1
    return n * recursiveFact(n-1)
