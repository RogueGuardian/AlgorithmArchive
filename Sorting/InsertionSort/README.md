# Insertion Sort

## Setup

### Input
Array/List A of comparable items

### Output
Array/List A of sorted items

## Pseudocode
```
signature: insertionSort(A)

i := 1
while i < length(A)
    j := i
    while j > 0 and A[j-1] > A[j]
        swap A[j], A[j-1]
        j := j-1
    done
    i := i + 1
done
```

## Runtime
- Worst Case: O(N^2) where N is the number of elements
- Average Case: Theta(N^2) where N is the number of elements
- Best Case: Omega(N) where N is the number of elements
