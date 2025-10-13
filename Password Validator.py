
while True:
    password_input = input("Please create your own passwords (at least 8 characters): ")
    if len(password_input) >= 8:
        print("Password valid !")
        break
    else:
        print("Password invalid ! Please try a new one follow the structured !")

    