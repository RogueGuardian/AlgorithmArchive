fn non_recursive_factorial(n: u64) -> u64 {
    let mut sum: u64 = 1;
    while n != 0 {
        sum *= n;
        n -= 1;
    }
    return sum;
}

fn recursive_factorial(n: u64) -> u64 {
    if n == 1 {
        return 1;
    }
    return n*recursive_factorial(n-1);
}
