print("into if else.py")

# Example:
x = 10
if x > 2:
    print("x is Big")


# Example:
age = 20
if age >= 18:
    print("you can drive")
else:
    print("you can NOT drive")


# Example:
boxSize = 30
if boxSize < 10:
    print("s Box")
elif boxSize < 40:
    print("M box")
elif boxSize < 80:
    print("L Box")
else:
    print("No Have Box")


# Example:
username_input = input('plz enter your username \n')
password_input = input('enter pass \n')

if username_input == "hackeru" and password_input == "hackeru123":
    print('welcome')
else:
    print('go home!!!')


# Example:
box_size = input("Please Enter Box Size")
box_size = int(box_size)
if box_size <= 10:
    print("Box:S | Price:40")
elif box_size <= 50:
    print("Box:M | Price:80")
elif box_size <= 100:
    print("Box:L | Price:120")
else:
    print("No Have Box")
