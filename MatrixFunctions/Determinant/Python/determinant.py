def det(M):
    if(len(M) != len(M[0])):
        return "ERROR"
    thisSum = 0
    for i in range(len(M)):
        thisSum += M[1][i] * ((-1)**(1+i)) * det(major(M, 1, i)
    return thisSum

def major(A, x, y):
    newM = []
    for i in range(len(A)):
        tempList = []
        for j in range(len(A)):
            if(i != x and j != y):
                tempList.append(A[i][j])
        if(tempList != []):
            newM.append(tempList)
    return newM
