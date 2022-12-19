# Task 3
+ [Problem 1](#problem-1)
+ [Problem 2](#problem-1)
+ [Problem 3](#problem-1)
+ [Problem 4](#problem-1)
+ [Problem 5](#problem-1)
+ [Problem 6](#problem-1)
+ [Problem 7](#problem-1)
+ [Problem 8](#problem-1)
+ [Problem 9](#problem-1)
+ [Problem 10](#problem-1)
+ [Problem 11](#problem-1)
+ [Problem 12](#problem-1)
+ [Problem 13](#problem-1)
+ [Problem 14](#problem-1)
+ [Problem 15](#problem-1)
+ [Problem 16](#problem-1)

## Problem 1
Найти все числа от 1 до 1000, которые делятся на 17.

```python
ans = [num for num in range(1001) if num % 17 == 0]
```

## Problem 2
Найти все числа от 1 до 1000, которые содержат в себе цифру 2.

```python
ans = [num for num in range(1, 1001) if num % 10 == 2 or num // 10 % 10 == 2 or num // 100 % 10 == 2]

ans = [num for num in range(1000) if '2' in str(num)]

```


## Problem 3
Найти все числа от 1 до 10000, которые являются палиндромом.

```python
ans = [num for num in range(1, 10001) if str(num) == str(num)[::-1]]
```


## Problem 4
Посчитать количество пробелов в строке.

```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
ans = len([sign for sign in string if sign == ' '])

```



## Problem 5
Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова

```python
str = "fserdhjdsnVFTRBRvkjdfsru"
ans = str.translate({ord(i): None for i in 'aeiouAEIOU'})
```



## Problem 6
На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5

```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
ans = [word for word in string.split() if len(word) < 6]
```




## Problem 7
На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.


```python
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
ans = {word: len(word) for word in string.split()}
```



## Problem 8
На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.


```python
string = "fcnreakjseADFHYTvn37y4rhbav"
ans = list(set([sign for sign in string.lower() if ord(sign) >= ord('a') and  ord(sign) <= ord('z') ]))
```


## Problem 9
На входе список чисел, получить список квадратов этих чисел / use map


```python
numbers = [3, 5, 6, 8]
ans = list(map(lambda x: x * x, numbers))

```



## Problem 10
На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2. На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)


```python
points = [(1, 1), (2, 3), (5, 3), (1, 3), (0, -2), (-5, 9)]
ans = {point: (point[0]**2 + point[1]**2)**(1/2) for point in points if point[0]*5 - 2 == point[1]}
```



## Problem 11
Возвести в квадрат все чётные числа от 2 до 27. На выходе список.

```python
ans = [num ** 2 for num in range(2, 28, 2)]
```




## Problem 12
На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти.


```python
points = [(1, 1), (2, 3), (5, 3), (1, 3), (0, -2), (-5, 9)]
ans = max([(point[0]**2 + point[1]**2)**(1/2) for point in points if point[0]>=0 and point[1 >= 0]])
```




## Problem 13
На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...]

```python
nums_first = [1, 2, 3, 5, 8] 
nums_second = [2, 4, 8, 16, 32]
ans = [(nums_first[i] + nums_second[i], nums_first[i] - nums_second[i]) for i in range(len(nums_first))]
```




## Problem 14

На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.


```python
numbers = ['43141', '32441', '431', '4154', '43121']
ans = [str(int(num)**2) for num in numbers if int(num) % 2 == 0]

```



## Problem 15
Менеджер как обычно придумал свое представление данных, а нам оно не подходит

input_str = """name,Petya,Vasya,Masha,Vova grade,5,5,8,3 subject,math,language,physics,math year,1999,2000,1995,1998"""

Мы хотим получить нормальную таблицу, чтобы импортировать в csv

[ { 'name': 'Petya', 'grade': '5' 'subject': 'math' 'year': '1999' }, { 'name': 'Vasya', 'grade': '5' 'subject': 'language' 'year': '2000' }, ... ]


```python

ans = [{line.split(',')[0]: line.split(',')[i] for line in input_str.split('\n')} for i in range(1, len(input_str.split(
    '\n')[0].split(',')))]

```



## Problem 16
Получить сумму по столбцам у двумерного списка

a = [[11.9, 12.2, 12.9], [15.3, 15.1, 15.1], [16.3, 16.5, 16.5], [17.7, 17.5, 18.1]]

result = [61.2, 61.3, 62.6]

```python
result = [sum(a[i][j] for i in range(len(a))) for j in range(len(a[0]))]
```
