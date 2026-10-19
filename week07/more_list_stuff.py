from random import randint, seed

seed(5)
lst = [randint(0,10) for _ in range(20)]

print(lst)
print(lst.count(1))
x = lst.index(10)
print(x)
print(lst[x])
print(max(lst), min(lst), sum(lst))

mx = -1
for i in lst:
    if i > mx:
        mx = i
    print(i, mx)

'''lst = [x for x in range(10)]
print(lst)
lst2 = [x for x in range(10, 21)]
print(lst2)
lst.extend(lst2)
print(lst)'''

'''lst.append(lst2)
lst2.append(21)
print(lst)
print(lst[-1])
lst2.pop()
print(lst)
print(lst2)'''

'''for i in range(len(lst)):
    lst[i] = str(lst[i])
print(lst)'''


alpha = list('cba')
print(alpha)
alpha.sort()
print(alpha)
alpha.sort(reverse=True)
print(alpha)