
alpha_one = 'abc'
alpha_two = 'xyz'

# new_st = alpha_one + alpha_two
new_st = alpha_one + " " + alpha_two
print(new_st)

last_alpha_one = alpha_one[-1]
last_alpha_two = alpha_two[-1]

new_st = alpha_one[:2] +last_alpha_two + alpha_two[:2] + last_alpha_one
# abzxyc
print(new_st)

print(new_st[1:-1])
alpha_three = new_st[1:-1]
print(new_st)
new_st = 'abcxyz'
print(alpha_three, new_st)