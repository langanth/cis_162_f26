
lst = [1, 2, 3]

print(lst[1])

d = {"A": 65, "B": 66, "C": 67}
print(d["A"])

d["A"] = 97
print(d["A"])
print(d)
del d["A"]
print(d)
d["A"] = 65
print(d)

# print(d["D"])
print(d.get('D'))
print(d.get('D', -1))

print(d)
#d.clear()
print(d)

d2 = {'D': 68, 'E': 69, 'F': 70}
print(d)
print(d2)
d.update(d2)
print('='*25)
print(d)
print(d2)
print('='*25)
d2['G'] = 71
d.update(d2)
print(d)
print(d2)

d['A'] = 97
print(d)
print(d2)
d2['A'] = 65

d.update(d2)
print(d)
print(d2)