func nonRecursiveGCD(a int, b int) int {
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
    if b == 0 {
        return a
    }
    return recursiveGCD(b, a%b)
}
