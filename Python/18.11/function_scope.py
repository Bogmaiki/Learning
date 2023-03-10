print("into functions scope")

print("*********** Example Local & Global ***********")

num1 = 10
num2 = 20

def plus1():
    print(num1+num2)  # 10 + 20

plus1()

def plus2():
    num2 = 2
    print(num1+num2)  # 10 + 2

plus2()

def plus3():
    num1 = 1
    num2 = 2
    print(num1+num2)  # 1 + 2

plus3()

print("*********** Example ***********")
num = 1000
print(num)


def michael():
    global num
    num = 5
    print(num)

def plus100():
    global num  # change global var
    num = num + 100
    print(num)

def plus10():
    global num  # change global var
    num += 10  # (num = num + 10)
    print(num)

michael()
plus10()
plus100()
num += 5  # (num = num + 5) >>>  change global var
print(num)

