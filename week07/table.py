from time import sleep


'''for m in range(60):
    for s in range(60):
        if s == 3:
            continue
        print(f'{m:02d}:{s:02d}')
        sleep(1)

        if s == 10:
            break
    if m == 10:
        break'''

for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print('done')


st = 'abcdefg'

for i, v in enumerate(st):
    print(i, v)