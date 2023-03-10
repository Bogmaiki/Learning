def ex1():
    words = int(input("Enter word count: "))
    sentance = ""
    for i in range (0, words):
        sentance += input("enter a word: ") + " "
    print(sentance)

def ex2():
    sum = 0
    for i in range (1,6):
        sum += int(input("Enter price: "))
    print(sum)

def ex3():
    num = int(input("Enter a number: "))
    sum = 0
    for i in range (1,num+1):
        sum += i
    print(sum)

def ex4():
    sum = 0
    price = int(input("Enter price: "))
    while price != 0:
        sum += price
        price = int(input("Enter price: "))
    print(sum)

