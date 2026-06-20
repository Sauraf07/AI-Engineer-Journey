'''Task 2: Student Marks Validator
Requirements

Ask user for marks.

Rules:

Marks must be between 0 and 100
If marks < 0 or > 100 raise custom error'''
class InvalidMarksError(Exception):
    pass
def validate_marks():
    while True:
        try:
            marks = float(input("Enter the marks (0-100): "))
            if marks < 0 or marks > 100:
                raise InvalidMarksError("Marks must be between 0 and 100.")
            print(f"Valid marks entered: {marks}")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
        except InvalidMarksError as ime:
            print(f"Invalid marks error: {ime}. Please try again.")
if __name__ == "__main__":
    validate_marks()