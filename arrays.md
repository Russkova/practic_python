# Arrays
+ [Merge two sorted array](#merge-two-sorted-array)
+ [Squares of sorted array](#squares-of-sorted-array)
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
