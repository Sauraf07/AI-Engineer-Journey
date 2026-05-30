# Task 10
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd Number : "))
o = input("Choose the operation : +,-,/,* : ")
match o:
    case "+":
        print(f"Addition : {a+b}")
    case "-":
        print(f"Sub : {a-b}")
    case "/":
        print(f"Divide : {a/b}")
    case "*":
        print(f"Multiple : {a*b}")
    case _:
        print("Enter a valid operation")
