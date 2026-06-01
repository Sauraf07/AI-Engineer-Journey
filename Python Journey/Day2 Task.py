# Task 1
'''num = int(input("Enter any no. : "))
if num%2==0:
    print("Even")
else:
    print("Odd")'''
# =============================================
# Task 2
'''a = int(input("Enter the 1st no. "))
b = int(input("Enter the 2nd no. "))
c = int(input("Enter the 3rd no. "))
if a>b and a>c: 
    print(f"{a} is grater ")
elif b>c:
    print(f"{b}  is Grater ")
else:
    print(f"{c} is Grater " )'''
# ===============================================
# Task 3
'''num = int(input("Enter the no. to print the table? "))
for i in range(11):
    print(f"{num} * {i} = {num*i}")'''
# =============================================
# Task 4
'''sum = 0
for i in range(101):
    sum += i

print(sum)'''
# ==========================================
# Task 5
'''num = int(input("Enter the no. "))
fact = 1
for i in range(1,num + 1):
    fact =  i * fact
print(fact) '''
# ===========================================
# Task 6
'''import random
s_num = random.randint(1,100)
print("Welcome to the Number Gussing Game!")
print("Guess a number between 1 and 100")
while True:
    guess = int(input('enter your guess: '))
    
    if guess > s_num:
        print("Too high")
    elif guess < s_num:
        print("Too low")
    else:
        print("Congrats ! You guess the no.")'''
# ======================================================
# Task 7
'''def add():
    num = int(input("Enter the 1st num "))
    num2 = int(input("Enter the 2nd num "))
    print(f"Addition {num+num2}")

def sub():
    num = int(input("Enter the 1st num "))
    num2 = int(input("Enter the 2nd num "))
    print(f"Substarction {num-num2}")

def multiply():
    num = int(input("Enter the 1st num "))
    num2 = int(input("Enter the 2nd num "))
    print(f"Multiplication {num*num2}")

def div():
    num = int(input("Enter the 1st num "))
    num2 = int(input("Enter the 2nd num "))
    print(f"Div {num/num2}")

add()
sub()
multiply()
div()
'''
# ====================================================
# Task 8
'''password = 12345
attend = 3
while attend > 0:
    ps = int(input("Enter password "))

    if ps == password:
        print("Access granted ")
        break
    else:
        attend -=1
        print("Incorrect password! Try again")

if attend == 0:
    print("Access dined")'''
# ====================================================
# Task 9
'''num = int(input("Enter a number : "))
if num <=1 :
    print("Not Prime ")
else:
    is_prime = True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            is_prime == False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")'''
# ====================================================
# Task 10
n = int(input("Enter number : "))
a,b = 0,1
for i in range(n):
    print(a,end=' ')
    a,b = b, a+b