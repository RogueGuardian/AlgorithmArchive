func insertionSort(A []int) {
    i := 1
    for i < len(A) {
        j := i
        for (j > 0) && (A[j-1] > A[j]) {
            A[j], A[j-1] = A[j-1], A[j]
            j--
        }
        i++
    }
}
