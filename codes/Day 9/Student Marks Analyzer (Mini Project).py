'''Task 5: Student Marks Analyzer (Mini Project)
Objective

Create a program that:

Accepts multiple student marks using *args
Calculates average
Finds highest mark
Finds lowest mark
Displays result'''
def analyze_marks(*args):
    if not args:
        return "No marks provided."
    
    average = sum(args) / len(args)
    highest = max(args)
    lowest = min(args)
    
    return {
        "average": average,
        "highest": highest,
        "lowest": lowest
    }

# Example usage
marks = analyze_marks(85, 90, 78, 92, 88)
print(marks)

