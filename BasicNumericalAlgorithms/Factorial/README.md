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
