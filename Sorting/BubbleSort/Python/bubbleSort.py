def bubbleSort(arr):
    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr)-1-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if(not swapped):
            break
