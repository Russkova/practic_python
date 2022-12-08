# Задание 1. Сумма диагональных эдементов матрицы.
def diagonalSum(mat):
    result = 0
    n = len(mat)
    for i in range(n):
        result += mat[i][i]
        result += mat[n - i - 1][i] if n - i - 1 != i else 0
    return result


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

# print(diagonalSum(mat))
# Задание 2. Объединение двух отсортированных строк


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


first = [1, 20, 30]
second = [30, 40]

# print(merge(first, second))

# Задание 3. Дан отсортированный список в неубавющем порядке. Вернуть элементы этого списка возведенные в квадрат в неубывающем порядке


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



s = [-30, -10, -2, 0, 1, 5, 20]
#print(squares(s))

# Задание 4.


def compress(elems):
    res = ""
    i, j = 0, 0
    while i < len(elems):
        while j < len(elems) and elems[i] == elems[j]:
            j += 1
        res = res + str(elems[i]) if i == j - 1 else res + str(elems[i]) + str(j-i)
        i = j
    return res
chrs = ["a","b","b","c","c","d"]
print(compress(chrs))


