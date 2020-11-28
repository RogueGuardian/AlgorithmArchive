def det(M):
    if(len(M) != len(M[0])):
        return "ERROR"

    thisSum = 0

    for i in range(len(M)):
        thisSum += M[0][i] * ((-1)**(1+i)) * det(major(M, 0, i)

    return thisSum
