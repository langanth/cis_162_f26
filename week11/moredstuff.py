d = {i: i * 2 for i in range(3)}
print(d)

for i in d.keys():
    if i == 0:
        d[i + 5] = i

print("okay?")