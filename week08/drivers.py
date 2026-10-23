drivers = {
    "Lewis Hamilton": [44,"Ferrari", 229],
    "Charles Leclerc": {"Number":16,"Team": "Ferrari", "Points": 215},
    "George Russell": [63, "Mercedes", 238],
    "Kimi Antonelli": [12,"Mercedes",340]
}

print(drivers["Lewis Hamilton"])
#print(drivers["George Russell"][1])
print('----------------')
print(drivers["Charles Leclerc"]["Number"])
print('----------------')
for i in drivers:
    print(i)

for i in drivers.values():
    print(i)