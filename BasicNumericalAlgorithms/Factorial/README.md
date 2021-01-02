# Factorial

## Setup

### Input
Integer n

### Output
n!

## Pseudocode

### Non Recursive
```
signature: fact(n)

fact := 1
while n != 0 do
    fact := fact * n
    n := n - 1
done
```

### Recursive
```
signature: fact(n)

if n == 1 then
    return 1
endif
return n * fact(n-1)
```

## Runtime
- Theta(N) where N is the value of the input
- Theta(2^B) where B is the number of bits of the binary representation of N
