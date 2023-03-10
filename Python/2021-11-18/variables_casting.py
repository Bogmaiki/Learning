print("into Variables_casting.py")
'''
int()
float()
str()
'''
# Example
x = int("10") # 10
print(x)
x = int(10.5) # 10
print(x)
x = int(10)  # 10
print(x)
# x = int("10.5") # Error - cant use int() on float string


# Example
y = float(10) # 10.0
print(y)
y = float(10.5) # 10.5
print(y)
y = float("10") # 10.0
print(y)
y = float("10.5") # 10.5
print(y)

# Example
z = str("Gal") # "Gal"
print(z)
z = str(10) # "10"
print(z)
z = str(10.5) # "10.5"
print(z)


# Example
str1 = "5"
print(int(str1) + 10) # 15

# Example
str2 = "10.5"
print(float(str2) + 10) # 20.5

# Example
total = 120
print("Total price is: " + str(total))


