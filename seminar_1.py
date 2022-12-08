# задача 1. Вывести числа от 1 до n, заменяя делящиеся на 3 и/или 5 на строки hello, world, helloworld.
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

# Задача 2. Длина максимальной подпоследовательности из единиц.

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

# Задача 3.
# Вход: nums = [0,1,2,4,5,7] # [0, 1, 2], [4, 5], [7]
# Выход: ["0->2","4->5","7"]

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






sumRanges([0, 6, 7, 9])

#helloWorld(20)
#print(ones( [1,0,1,1,1,0]))