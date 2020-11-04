# Bubble Sort

## Setup

### Input
Array/List A of comparable items

### Output
Array/List A of sorted items

## Pseudocode
```
for i := 0 to n do
    for j := 0 to n-i-1 do
        if A[j] > A[j+1] then
            swap A[j], A[j+1]
        endif
    done
done
```
