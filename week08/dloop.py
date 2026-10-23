from string import ascii_uppercase
d = {k: ord(k) for k in ascii_uppercase}
print(d)

for i in d.keys():
    print(f'key={i}, value={d[i]}')

for v in d.values():
    print(v)

for i in d.items():
    print(i, i[0], i[1])

for k, v in d.items():
    print(k, v)