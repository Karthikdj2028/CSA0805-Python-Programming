# 7. Customer billing with discount
name, mobile, cost = "John", "9876543210", 1000
discount_rate = 0.1
discount = cost * discount_rate
total = cost - discount
print(f"Customer: {name}")
print(f"Mobile: {mobile}")
print(f"Cost of purchase: {cost}")
print(f"Discount: {discount}")
print(f"Total amount to be paid: {total}")