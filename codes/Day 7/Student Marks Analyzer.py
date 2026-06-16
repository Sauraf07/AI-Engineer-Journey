'''Task 4: Student Marks Analyzer
Objective

Practice loops with lists.

Requirements

User enters 5 marks.

Program calculates:

Highest mark
Lowest mark
Average mark'''
marks = []
for i in range(5):
    mark = float(input(f"Enter mark {i + 1}: "))
    marks.append(mark)
highest_mark = max(marks)
lowest_mark = min(marks)
average_mark = sum(marks) / len(marks)
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Average Mark: {average_mark:.2f}")
