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
