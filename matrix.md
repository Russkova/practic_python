# Matrix

+ [Diagonal sum](#diagonal-sum)


## Diagonal sum

Сумма диагональных эдементов матрицы.

```python
diagonalSum(mat):
    result = 0
    n = len(mat)
    for i in range(n):
        result += mat[i][i]
        result += mat[n - i - 1][i] if n - i - 1 != i else 0
    return result

```
