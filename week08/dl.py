
lst = [i for i in range(10)]

print(lst)
print(lst.pop())
print(lst)
'''lst.remove(2)
lst.remove(2)'''
x = lst.pop(2)
y = lst.pop(2)
print(lst)
print(x, y)

j = 0
while j < 5:
    k = lst.pop(3)
    lst.insert(0, k)
    print(lst)
    j += 1

'''for i in lst:
    print(i[-1])

for i in range(len(lst)):
    print(lst[i][-1])'''

