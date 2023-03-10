# EX 1
password = input("Please enter password: ")
if (password == "hacker123" ):
    print("Welcome")
else:
    print("Wrong password")

# EX 2
user_name = input("Please enter username: ")
password2 = input("Please enter password: ")
if (user_name == "hackeru" and password2 == "hacker123"):
    print("Welcome")
else:
    print("Incorrect username or password")

# EX 3
age = int(input("Enter your age: "))
if (age < 16):
    print("You can't drive")
elif(age >= 16):
    print("You can take driving lessons")

# EX 4
age2 = int(input("Enter your age: "))
if (age2 <= 16):
    print("You can't drive")
elif(age2 > 16 and age2 <= 18):
    print("You can take driving lessons")
elif(age2 > 18 and age2 < 70):
    print("You can drive")
elif(age2 >= 70):
    print("You can drive with a doctor's approval")

# EX 5
size = int(input("Enter your pants size: "))
if (size >= 24 and size <= 30):
    print("your size is: S")
elif (size >= 31 and size <= 36):
    print("your size is: M")
elif (size > 36):
    print("your size is: L")
else:
    print("We're sorry, we don't have this size")

# EX 6
num = int(input("Enter a number: "))
if (num%2 == 0):
    print("the number is even")
else:
    print("the number is not even")

# EX 7
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
op = input("enter if + or * :")
if (op == "+"):
    print(num1 + num2)
elif (op == "*"):
    print(num1 * num2)
else:
    print("Error")

# EX 8
user_name2 = input("Enter username: ")
password3 = input("Enter password: ")
if (user_name2 == "" and password3 == ""):
    print("You have to enter username and password")
elif (password3 == ""):
    print("You have to enter a password")
elif (user_name2 == ""):
    print("You have to enter a username")
else:
    if (user_name2 == "haackeru" and password3 == "hacker123"):
        print("Welcome")
    else:
        print("incorrect username or password")