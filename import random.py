import random 
secret_number= random.randint(1, 10)

print("I'm thinking of a number between 1 and 10.")
print("can you guess what it is ?")

guess = 0
attempts = 0

while guess != secret_number:
    try:
        user_input = input("Enter your guess: ")
        guess = int(user_input)
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Yay ! You've got it {secret_number} in {attempts}")
    except ValueError:
        print("That's not a valid number !")
        
        continue


