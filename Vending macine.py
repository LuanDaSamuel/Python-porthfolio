item_price = 2.5

money_inserted_from_user = input("Please insert your money: ")
money_inserted = float(money_inserted_from_user)

if money_inserted == item_price:
    print(f"Exact amount received. Enjoy your item!")
elif money_inserted > item_price:
    change_amount = money_inserted - item_price
    print(f"Enjoy your item! Here is your change:{change_amount}")
else:
    remaining_needed = item_price - money_inserted
    print(f"Insufficient funds. You need {remaining_needed} more. Money returned.")