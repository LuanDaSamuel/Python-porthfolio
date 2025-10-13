item_delivery = 120000
plus_delivery_fee = 5000


if item_delivery >= 100000:
    result = item_delivery * (1 - 0.1)
    print(f"The result of {item_delivery} * {1 - 0.1}: {result}")
elif item_delivery >= 300000:
    result = item_delivery * (1 - 0.2)
    print(f"The result of {item_delivery} * {1 - 0.2}: {result}")

if result < 150000:
    total = result + 5000
    print(f"The restult of {result} + {5000}: {total}")
else:
    total = result + 0
    print(f"The restult of {result} + {0}: {total}")

print("Bill")

print(result)
print(plus_delivery_fee)
print("total bill that you have to pay:")
print(total)