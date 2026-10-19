
st = 'abcdefg'
x = 0

for i in range(len(st)):
    print(st[i])

for i in st:
    print(i)

while x < len(st):
    print(st[x])
    x += 1

for i in st:
    print(i * 2)

for i in range(0, 10):
    print(i)

for i in range(len(st) - 1, -1, -1):
    print(i, end='')


st = 'hello'
for i in st:
    print(i)
