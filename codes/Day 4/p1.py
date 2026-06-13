# Task 1: Student Marks Manager (Easy)
'''Print all marks
Print highest mark
Print lowest mark
Print average mark
Add a new mark
Remove a mark'''
marks = [85, 90, 78, 92, 88]
def print_marks():
    print("Marks:", marks)
def print_highest_mark():
    print("Highest Mark:", max(marks))
def print_lowest_mark():
    print("Lowest Mark:", min(marks))
def print_average_mark():
    print("Average Mark:", sum(marks) / len(marks))
def add_mark(mark):
    marks.append(mark)
def remove_mark(mark):
    marks.remove(mark)
# Example usage
print_marks()
print_highest_mark()
print_lowest_mark()
print_average_mark()
add_mark(95)
print_marks()
remove_mark(78)
print_marks()

