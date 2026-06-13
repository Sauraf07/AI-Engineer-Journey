# Task 5: Smart Unit Converter (Challenge)
print("Welcome to the Smart Unit Converter!")
print("\nSelect the type of conversion:")
print("1. Length")
print("2. Weight")
print("3. Temperature")
conversion_type = input("Enter choice (1/2/3): ")
if conversion_type == '1':
    print("\nLength Conversion:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    length_choice = input("Enter choice (1/2): ")
    if length_choice == '1':
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is equal to {feet:.2f} feet.")
    elif length_choice == '2':
        feet = float(input("Enter length in feet: "))
        meters = feet / 3.28084
        print(f"{feet} feet is equal to {meters:.2f} meters.")
    else:
        print("Invalid input. Please select a valid conversion.")
elif conversion_type == '2':
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    weight_choice = input("Enter choice (1/2): ")
    if weight_choice == '1':
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kg is equal to {pounds:.2f} lbs.")
    elif weight_choice == '2':
        pounds = float(input("Enter weight in pounds: "))
        kilograms = pounds / 2.20462
        print(f"{pounds} lbs is equal to {kilograms:.2f} kg.")
    else:
        print("Invalid input. Please select a valid conversion.")
elif conversion_type == '3':
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    temp_choice = input("Enter choice (1/2): ")
    if temp_choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
    elif temp_choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
    else:
        print("Invalid input. Please select a valid conversion.")
else:
    print("Invalid input. Please select a valid conversion type.")