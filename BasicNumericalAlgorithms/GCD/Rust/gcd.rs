fn non_recursive_gcd(a: u32, b:u32) -> u32 {
    // Return 0 if a or b is invalid
    if a < 1 || b < 1 {
        return 0
    }

    // Case where GCD is 1
    if a == 1 || b == 1 {
        return 1
    }
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
    // Return 0 if a or b is invalid
    if a < 1 || b < 1 {
        return 0
    }

    if b == 0 {
        return 1;
    }
    return recursive_gcd(b, a % b);
}
