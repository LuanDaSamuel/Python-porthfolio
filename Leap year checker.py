Year_input = input("Enter a year: ")
Year = int(Year_input)

if Year % 400 == 0:
    print("Leap year")
elif Year % 4 == 0 and not Year % 100 == 0:
    print("Leap year")
else:
    print("Not a leap year")