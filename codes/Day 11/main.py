from student_package.marks import total_marks
from student_package.grade import calculate_grade

def calculate_average(marks):
    total = total_marks(marks)
    average = total / len(marks)
    return average

def calculate_final_grade(marks):
    average = calculate_average(marks)
    grade = calculate_grade(average)
    return grade

def main():
    marks = [85, 90, 78, 92, 88]
    average = calculate_average(marks)
    final_grade = calculate_final_grade(marks)

    print("Marks:", marks)
    print("Average:", average)
    print("Final Grade:", final_grade)

if __name__ == "__main__":
    main()
    