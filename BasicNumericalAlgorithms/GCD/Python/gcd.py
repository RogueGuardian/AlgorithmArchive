def nonRecursiveGCD(a, b):
    while(a != b):
        if(a > b):
            a -= b
        else:
            b -= a
    return a

def recursiveGCD(a, b):
    if(b == 0):
        return a
    return recursiveGCD(b, a % b)
