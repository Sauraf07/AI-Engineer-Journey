'''Task 5: Weather Data Analyzer
Objective

Analyze weather records stored in a CSV file.

CSV Structure
Date,Temperature,Humidity
2026-06-01,34,60
2026-06-02,36,55
Features
Read CSV Data
Find Highest Temperature
Find Lowest Temperature
Calculate Average Temperature
Find Average Humidity
Bonus

Display the hottest day.'''

import csv
def read_weather_data():
    with open('weather_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def find_highest_temperature():
    with open('weather_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        highest_temp = float('-inf')
        hottest_day = ""
        for row in reader:
            date, temp, humidity = row
            temp = float(temp)
            if temp > highest_temp:
                highest_temp = temp
                hottest_day = date
        print(f"Highest Temperature: {highest_temp} on {hottest_day}")

def find_lowest_temperature():
    with open('weather_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        lowest_temp = float('inf')
        coldest_day = ""
        for row in reader:
            date, temp, humidity = row
            temp = float(temp)
            if temp < lowest_temp:
                lowest_temp = temp
                coldest_day = date
        print(f"Lowest Temperature: {lowest_temp} on {coldest_day}")

def calculate_average_temperature():
    with open('weather_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        total_temp = 0
        count = 0
        for row in reader:
            temp = float(row[1])
            total_temp += temp
            count += 1
        average_temp = total_temp / count if count > 0 else 0
        print(f"Average Temperature: {average_temp:.2f}")

def find_average_humidity():
    with open('weather_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        total_humidity = 0
        count = 0
        for row in reader:
            humidity = float(row[2])
            total_humidity += humidity
            count += 1
        average_humidity = total_humidity / count if count > 0 else 0
        print(f"Average Humidity: {average_humidity:.2f}")

def display_hottest_day():
    with open('weather_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        highest_temp = float('-inf')
        hottest_day = ""
        for row in reader:
            date, temp, humidity = row
            temp = float(temp)
            if temp > highest_temp:
                highest_temp = temp
                hottest_day = date
        print(f"Hottest Day: {hottest_day} with Temperature: {highest_temp}")

def main():
    while True:
        print("\nWeather Data Analyzer")
        print("1. Read Weather Data")
        print("2. Find Highest Temperature")
        print("3. Find Lowest Temperature")
        print("4. Calculate Average Temperature")
        print("5. Find Average Humidity")
        print("6. Display Hottest Day")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            read_weather_data()
        elif choice == '2':
            find_highest_temperature()
        elif choice == '3':
            find_lowest_temperature()
        elif choice == '4':
            calculate_average_temperature()
        elif choice == '5':
            find_average_humidity()
        elif choice == '6':
            display_hottest_day()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()