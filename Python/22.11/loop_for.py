print("into loop_for.py")

print("********** Example 1 **********")
for i in range(1, 11):  # range(1,11) >>  1-10
    print(i)



print("********** Example 2 **********")
for y in range(1, 11):
    print(11 - y)



print("********** Example 3 **********")
for x in range(0, 11):
    x += 1
    if x%3 == 0:
        continue  # continue ONLY ONE time
    print(x)



print("********** Example 4 **********")
for z in range(0, 11):
    z += 1
    if z%3 == 0:
        break  # break STOP the while
    print(z)



print("********** Example 5 **********")
for i in range(11):  # range(11) >>  0-10 >>
    print(i)



print("********** Example 6 **********")
for i in range(1, 11, 2):  # range(1,11,2) >>  1-10 >> 1,3,5,7,9
    print(i)



print("********** Example 7 **********")
for i in range(1, 11, 3):  # range(1,11,3) >>  1-10 >> 1,4,7,10
    print(i)


print("********** Example 8 **********")
for i in range(11, 1, -3 ):  # range(11, 1, -3) >>  11-2 >> 11,8,5,2
    print(i)



print("********** Example 9 **********")
for i in "Gal Lavi":  # G,a,l, ,L,a,v,i
    print(i)