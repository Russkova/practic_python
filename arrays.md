# Arrays
+ [Array compression](#array-compression)
+ [Subsequences of units](#subsequences-of-units)
+ [Merge two sorted array](#merge-two-sorted-array)
+ [Squares of sorted array](#squares-of-sorted-array)



## Array compression

 Вход: nums = [0,1,2,4,5,7] 
 
 Выход: ["0->2","4->5","7"]
```python
def sumRanges(lst):
    ans = []
    left = lst[0]
    right = None
    for i in range(len(lst) - 1):
        if lst[i+1] == lst[i] + 1:
            right = lst[i + 1]
        elif right == None:
            ans.append(str(left))
        else:
            ans.append(str(left) + "->" + str(right))
            left = lst[i+1]
            right = None
    if right == None:
        ans.append(str(left))
    else:
        ans.append(str(left) + "->" + str(right))
    print(ans)

```

## Subsequences of units

Длина максимальной подпоследовательности из единиц.

```python
def ones(lst):
    ans = 0
    cur = 0
    for i in lst:
        if i == 1:
            cur += 1
            if ans < cur:
                ans = cur
        else:
            cur = 0
    return ans
```

## Merge two sorted array

Слияние двух отсортированных массива в один отсортированный массив за О(n).

```python
def merge(first, second):
    n1, n2 = len(first), len(second)
    i, j = 0, 0
    ans = []
    while i < n1 and j < n2:
        if first[i] < second[j]:
            ans.append(first[i])
            i = i + 1
        else:
            ans.append(second[j])
            j = j + 1
    while i < n1:
        ans.append(first[i])
        i += 1
    while j < n2:
        ans.append(second[j])
        j += 1
    return ans

```
## Squares of sorted array
Дан отсортированный список в неубывающем порядке. Вернуть элементы этого списка, возведенные в квадрат в неубывающем порядке.

```python
def merge(first, second):
    n1, n2 = len(first), len(second)
    i, j = 0, 0
    ans = []
    while i < n1 and j < n2:
        if first[i] < second[j]:
            ans.append(first[i])
            i = i + 1
        else:
            ans.append(second[j])
            j = j + 1
    while i < n1:
        ans.append(first[i])
        i += 1
    while j < n2:
        ans.append(second[j])
        j += 1
    return ans


def squares(s):
    if s[0] >= 0:
        ans = [elem * elem for elem in s]
        return ans
    elif s[-1] <= 0:
        ans = [elem * elem for elem in s]
        return list(reversed(ans))
    else:
        for i in range(len(s)):
            if s[i] >= 0:
                s1 = [elem * elem for elem in s[:i]]
                s2 = [elem * elem for elem in s[i:]]
                return merge(list(reversed(s1)), s2)



```
