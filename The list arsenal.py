Baverage = ["Coca", "Beer", "Juice", "Water"]

Coca = 1 
Beer = 2
Juice = 3
Water = 4
print(Baverage)



userinput = Coca or Beer or Juice or Water
user = input("Which baverage i can get for you today: ")

if userinput == 1 :
    print(Baverage [0])
elif userinput == 2:
    print(Baverage [1])
elif userinput == 3:
    print(Baverage [2])
else:
    print(Baverage [-1])


Coca_cost = 2.5 
Beer_cost = 4
Juice_cost = 2
Water_cost = 2

same = Juice_cost or Water_cost

if Baverage == Coca:
    print(f"Your baverage cost: {Coca_cost} EURO")
elif Baverage == Beer:
    print(f"Your baverage cost: {Beer_cost} EURO")
else:
    print(f"Your baverage cost: {same} EURO")