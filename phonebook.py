phonebook = { "Dad": "090-373-4362", "Mom": "093-844-2068"}


while True:
    user = input("Enter a name to find number: ")
    if user in phonebook:
        print(f"This is your result {phonebook[user]}")
        break
    else:
        print("Invalid name, please try again !")
