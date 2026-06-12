# Task 5: BMI Calculator
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is: " + str(bmi))
under_weight_threshold = 18.5
over_weight_threshold = 25

if bmi < under_weight_threshold:
    print("You are underweight.")
elif bmi < over_weight_threshold:
    print("You are of normal weight.")
else:
    print("You are overweight.")