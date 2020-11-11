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
