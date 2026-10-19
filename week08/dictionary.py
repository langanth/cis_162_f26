
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