# Bubble Sort

## Setup

### Input
Array/List A of comparable items

### Output
Array/List A of sorted items

## Pseudocode
```
signature: bubbleSort(A)

for i := 0 to n do
    swapped := false
    for j := 0 to n-i-1 do
        if A[j] > A[j+1] then
            swap A[j], A[j+1]
            swapped := true
        endif
    done

    if not swapped then
        break
    endif
done
```

## Runtime
- Worst Case: O(N^2) where N is the number of elements
- Average Case: Theta(N^2) where N is the number of elements
- Best Case: Omega(N) where N is the number of elements
