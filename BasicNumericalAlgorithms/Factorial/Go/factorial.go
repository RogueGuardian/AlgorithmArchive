func nonRecursiveFactorial(n int) int {
    fact := 1
    for n != 0 {
        fact *= n
        n--
    }
    return fact
}

func recursiveFactorial(n int) int {
    if n == 1 {
        return 1
    }
    return n * recursiveFact(n-1)
}
