# String

+ [HelloWorld](#hellworld)
+ [String compression](#string-compression)

## HelloWorld

Вывести числа от 1 до n, заменяя делящиеся на 3 и/или 5 на строки hello, world, helloworld.

```python
def helloWorld(n):
    for i in range(n):
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print("helloworld")
        elif i % 3 == 0:
            print("hello")
        elif i % 5 == 0:
            print("world")
        else:
            print(i)

```

## String compression

in:

chrs = ["a","b","b","c","c","c"]

chrs2 = ["d","a","b","c"]

chrs2 = ["c","c","c"]


out:

"ab2c3"

"dabc"

"c3"

```python
def compress(elems):
    res = ""
    i, j = 0, 0
    while i < len(elems):
        while j < len(elems) and elems[i] == elems[j]:
            j += 1
        res = res + str(elems[i]) if i == j - 1 else res + str(elems[i]) + str(j-i)
        i = j
    return res
```
