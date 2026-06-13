# Task 3: BMI Calculator (Intermediate)
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
if height > 0:
    bmi = weight / (height ** 2)
    print("\nYour BMI is:", round(bmi, 2))
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
else:
    print("Error: Height must be greater than zero.")
    