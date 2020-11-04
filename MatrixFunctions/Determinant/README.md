# Determinant

## Input
2D Array of numerical values

## Out
Determinant value of the matrix

## Pseduocode
### Determinant
```
signature: det(arr)

if len(arr) != len(arr[0]) then
    throw error
endif
sum := 0
for i := 0 to n do
    sum += arr[1][i] * (-1)^(i+1) * det(major(arr, 1, i))
done
```

### Major
```
signature: major(arr, x, y)

newArr := []
for i := 0 to n do
    tempList := []
    for j := 0 to n do
        if i != x and j != y then
            tempList.append(arr[i][j])
        endif
    done
    if tempList != [] then
        newArr.append(tempList)
    endif
done

return newArr
```
