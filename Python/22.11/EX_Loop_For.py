# EX 1
for i in range (1,11):
    print(i)

# EX 2
for i in range (2,8):
    print(i)

# EX 3
for i in range (10,-1,-1):
    print(i)

# EX 4
for i in range (8,2,-1):
    print(i)

# EX 5
num = int(input("enter end number: "))
for i in range (0,num):
    print(i)

# EX 6
x = int(input("enter start number: "))
for i in range (x,101):
    print(i)

# EX 7
start = int(input("enter start number: "))
end = int(input("enter end number: "))
for i in range (start,end+1):
    print(i)

# EX 8
start2 = int(input("enter start number: "))
end2 = int(input("enter end number: "))
if start2 < end2:
    for i in range (start2,end2+1):
        print(i)
else:
    print("Error")