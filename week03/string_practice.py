
msg = input('Please enter your message here: ')

print(len(msg))
print(msg[0])
print(msg[len(msg) - 1]) #As long as the index is an integer, we can check it
print(msg[-1])
print(msg[::-1])
print(msg * 3)

change_msg = msg.replace('hate', 'love')
print(change_msg)
print(msg)

alt_msg = msg[::3]
print(alt_msg)

x = int(input())
y = int(input())

temp = x
x = y
y = temp


print(x, y) 

x = 1
y = 2

y, x = x, y