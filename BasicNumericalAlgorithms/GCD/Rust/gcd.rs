fn non_recursive_gcd(a: u32, b:u32) -> u32 {
    while a != b {
        if a < b {
            a -= b
        } else {
            b -= a
        }
    }
    return a;
}

fn recursive_gcd(a: u32, b: u32) -> u32 {
    if b == 0 {
        return 1;
    }
    return recursive_gcd(b, a % b);
}
