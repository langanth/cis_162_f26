

lst = list('abcdefg')
#lst = list(['abc', 'def', 'ghi'])
print(lst)
print(len(lst))
print(lst[0:3])
lst[0] = 'z'
# lst[7] = 'y'
lst.append('y')
print(lst)

lst.insert(0, 'a')
print(lst)
lst.append('a')
print(lst)
lst.remove('a')
print(lst)
# x = lst.pop()
x = lst.pop(2)
print(lst)
print(x)

'''for i in lst:
    print(i, end=' ')
    for j in i:
        print(j, end=' ')

    print()'''
