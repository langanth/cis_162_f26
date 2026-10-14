
def splice(val, sp):
    new_val = ''
    for i in val:
        new_val += i + sp
    return new_val

#st = input()
#sp = input()
lst = ['abc', 'def', 'hij']
sp = '/'

for i in lst:
    print(splice(i, sp))
#print(splice(st, sp))