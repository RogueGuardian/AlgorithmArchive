def insertionSort(A):
    i = 0
    while(i < len(A)):
        j = i
        while((j > 0) and (A[j-1] > A[j])):
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1
        i += 1
