
systems = []
st.lower()

def func(st):
    return st.lower()

print(func('ABC'))

while True:
    entry = input('Enter thing: ').strip().lower()
    print(entry)
    if entry == "stop":
        break
    if entry not in systems:
        systems.append(entry)

print(systems)