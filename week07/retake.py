import math

def bake_sale(customers):
    cookies_needed = customers * 3
    batches = math.ceil(cookies_needed / 18)
    total_cost = 7.75 * batches * 1.06
    return total_cost

print(bake_sale(6))
print(bake_sale(10))
print(bake_sale(20))

