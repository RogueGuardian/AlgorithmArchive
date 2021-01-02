func nonRecursiveGCD(a int, b int) int {
	// Return 0 when a or b are invalid
	if a < 1 || b < 1 {
		return 0
	}

	// Case where GCD is 1
	if a == 1 || b == 1 {
		return 1
	}

    for a != b {
        if a > b {
            a -= b
        } else {
            b -= a
        }
    }
    return a
}

func recursiveGCD(a int, b int) int {
	// Return 0 when a or b are invalid
	if a < 1 || b < 1 {
		return 0
	}

    if b == 0 {
        return a
    }
    return recursiveGCD(b, a % b)
}
