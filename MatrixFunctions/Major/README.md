# Major

## Input
2D Array of numerical values and specified coordinates

## Out
Major of that matrix at that location

## Pseduocode

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
