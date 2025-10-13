first_name = input("What is your name ?:  ")
last_name = input("What is your last name ?: ")
current_age = int(input("What is your current age ?: "))
current_year = 2025

name = first_name +" "+ last_name
born_year = current_year - current_age

print(f"Hello, what is your first name ? {first_name}")
print(f"And what is your last name ? {last_name}")
print(f"Nice to meet you, {name} ! How old are you ? {current_age}")
print(f"Great! So, {name}, you are {current_age} years old and were likely born in {born_year}")