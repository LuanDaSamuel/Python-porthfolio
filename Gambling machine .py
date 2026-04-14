import random

money=10
lost = 1
kasino = random.randint(1,10)

while money > 0:
    minun = int(input("Enter a number between 1 and 10: "))
    print(f"You got number {minun}")
    #vertaillaan kumpi suurempi
    if minun > kasino:
        print(f"You won ! {minun} is bigger than {kasino}")
        money = money + 2 * lost
        print(f"You have {money} money left.") 
    elif minun == kasino:
        print(f"Draw.")
        money =  money + lost
        print(f"You have {money} money left.")
    else:
        print(f"Kasino voitti!")
        money -= lost
        print(f"You have {money} money left.")
    continue
print(f"Game over. You have {money} money left.")
