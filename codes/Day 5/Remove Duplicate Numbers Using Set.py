'''Task 4: Remove Duplicate Numbers Using Set (Medium)
Objective

Use sets to remove duplicates.'''
numbers = [1,2,3,2,4,5,3,6,1]
unique_numbers = set(numbers)
print("Unique Numbers:")
for number in unique_numbers:
    print(dict(number=number))