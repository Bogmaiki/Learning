print("into function_return.py")

# Example
def return_hola_to():
    name1 = input("Enter name")
    return "Hola " + name1



x = return_hola_to()
print(x)

# Example
def plus():
    num1 = input("Please enter num1 ")
    num1 = int(num1)
    num2 = input("Please enter num2 ")
    num2 = int(num2)
    return num1 + num2

total = plus()
print(total)


def login():
    username_input = input('Enter username \n')
    password_input = input('Enter password \n')
    if username_input == "hackeru" and password_input == "hackeru123":
        is_login = True
    else:
        is_login = False
    return is_login

user1 = login()
print(user1)



user2 = login()
print(user2)