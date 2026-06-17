'''Task 4: Temperature Converter

Concepts Covered:

Functions
Mathematical Calculations'''
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
# Example usage:
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F.")
temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F is equal to {temp_c}°C.")

