# Euclid's GCD Algorithm

## Setup

### Input
Whole Numbers, a and b

### Out
Greatest common divisor of both a and b

## Pseudocode

### Non Recursive
```
signature: gcd(a, b)

while a != b
    if a < b then
        a := a - b
    else
        b := b - a
    endif
done
```

### Recursive
```
signature: gcd(a, b)

if b == 0 then
    return a
endif

return gcd(b, b mod a)
```
