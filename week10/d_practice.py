
d = {k: k*2 for k in range(10)}
print(d)


keys = d.keys()
values = d.values()
itms = d.items()
print(keys)
print(values)
print(itms)

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
    print(k, v, end='\t')

print()
music = {}

music["Streetlight Manifesto"] = {"Album": "Everything Goes Numb", 
                                  "Release": 2003, 
                                  "Songs": ["Everything Went Numb", "That'll be the Day", "Point/Counterpoint"]}

print(music["Streetlight Manifesto"]["Release"])

for i in music:
    print(i)

grid = []

coords = {}

for i in range(len(grid)):
    for j in range(len(grid[i])):
        coords[(i, j)] = grid[i][j]

tpl = (1, 2, 3)

def create_tpl(x, y):
    return x, y

print(create_tpl(1, 2))