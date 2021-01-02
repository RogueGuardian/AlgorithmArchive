func nonRecursiveFactorial(n int) int {
	// Returning -1 when n is not valid
	if n < 0 {
		return -1
	}

    fact := 1
    for n != 0 {
        fact *= n
        n--
    }
    return fact
}

func recursiveFactorial(n int) int {
	// Returning -1 when n is not valid
	if n < 0 {
		return -1
	}

    if n == 0 {
        return 1
    }
    return n * recursiveFact(n-1)
}
