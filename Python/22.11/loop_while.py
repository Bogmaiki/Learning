print("into loop_while.py")




print("********** Example **********")
i = 1
while i <= 10:
    print(i)
    i += 1



print("********** Example **********")
y = 10
while y >= 1:
    print(y)
    y -= 1



print("********** Example **********")

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("Boom!")  # will run one time when the condition is False



print("********** Example - end  **********")
end = int(input("Enter end number"))
x = 1
while x <= end:
    print(x)
    x += 1



print("********** Example - continue **********")
x = 0
while x <= 10:
    x += 1
    if x % 3 == 0:
        continue  # continue ONLY ONE time
    print(x)



print("********** Example - break **********")
z = 0
while z <= 10:
    z += 1
    if z % 3 == 0:
        break  # break STOP the while
    print(z)



print("********** Example **********")


user_user = input('enter user')
user_pass = input('enter pass')

while user_user != "hackeru" or user_pass != "hackeru123":
    user_user = input('enter user')
    user_pass = input('enter pass')
