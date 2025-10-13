secreat_number = "Sam100"
user_guess = ""

while user_guess != secreat_number:
    user_guess = input("Enter the password: ")

    if user_guess == secreat_number:
        print("Access granted")
        break
    else:
        print("Password incorrect, please try again.")
        