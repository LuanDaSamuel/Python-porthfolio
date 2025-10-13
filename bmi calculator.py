weight_in_kg = float(input("What is your current weight: "))
height_in_meter = float(input("What is your current height: "))


BMI = weight_in_kg / (height_in_meter * height_in_meter)

if BMI < 18.5:
    print("Underweight")
elif BMI <= 24.9:
    print("Normal weight")
elif BMI <= 29.9:
    print("Overweight")
else:
    print("Obesity")