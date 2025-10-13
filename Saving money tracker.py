goal_amount = 1500000
monthly_saving = 50000
current_saving = 0
month_taken = 0

print("Welcome to your Savings Goal Tracker !")
print(f"Your goal is to save {goal_amount}.")
print(f"You save {monthly_saving} each month.")
print("-" * 30)

while current_saving < goal_amount:
    current_saving = current_saving + monthly_saving
    month_taken = month_taken + 1
    print(f"After month {month_taken}: current_saving = {current_saving}")

print("-"  * 30)
print(f"Congratulations ! You reached your goal of {goal_amount}!")
print(f"It took you {month_taken} months and your final savings are {current_saving}.")

print("Calculating to year....")
print("Analyze...")

year = month_taken // 12
remaining_month = month_taken % 12


if year > 0 and remaining_month > 0:
    print(f"It took you {year} years and {remaining_month} months to save {goal_amount}.")
elif year > 0 and remaining_month == 0:
    print(f"It took you exactly {year} years to save {goal_amount}.")
else:
    print(f"Congratulation for you goal of {goal_amount}")