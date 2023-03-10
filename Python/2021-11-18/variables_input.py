print("into Variables_casting.py")
'''
input()
use \n for new line 
'''

# Example 1
first_name = input('plz enter your first name \n')
print("Hola " + first_name)


# Example 2
first = input('please enter your first name \n')
last = input('Please enter enter last name \n')
print("Hola " + first + " " + last)


# Example 3
num1 = input("Please Enter num1")
num2 = input("Please Enter num2")
total = num1 + num2  # without casting we get long string
print(total)

total = int(num1) + int(num2)  # with casting we get sum of numbers
print(total)



total = int(input("Enter num1 ")) + int(input("Enter num2"))
print(total)


