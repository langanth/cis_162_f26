


d = {k: k / 2 for k in range(10)}
print(d)

for k in d.keys():
    print(k, end=' ')
print()

for v in d.values():
    print(v, end=' ')
print()

for i in d.items():
    print(i, end=' ')
print()

for k, v in d.items():
    print(k, end=' ')
    print(v, end='\t')
print()

# print(d[-1])
print(d.get(-1))
print(d.get(-1, 'NOT FOUND'))