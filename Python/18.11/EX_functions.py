def hola ():
    name = input("enter first name: ")
    print("Hola " + name)

def shalom():
    fName = input("enter first name: ")
    lName = input("enter last name: ")
    print("Shalom " + fName + " " + lName)

def welcome():
    fName = input("enter first name: ")
    lName = input("enter last name: ")
    print("Hello " + fName + " " + lName + "you are welcome")

def plus():
    num1 = int(input("enter number: "))
    num2 = int(input("enter another number: "))
    print(num1 + num2)

def plusPlus():
    price1 = int(input("enter first price: "))
    price2 = int(input("enter second price: "))
    price3 = int(input("enter third price: "))
    print(price1 + price2 + price3)

def market():
    price1 = int(input("enter first price: "))
    price2 = int(input("enter second price: "))
    price3 = int(input("enter third price: "))
    print(price1 + price2 + price3 + 20)

def superMarket():
    price1 = int(input("enter first price: "))
    price2 = int(input("enter second price: "))
    price3 = int(input("enter third price: "))
    print(price1 + price2 + price3)
    discount= int(input("enter discount amount: "))
    print(price1 + price2 + price3 - discount)

def isBig():
    num1 = int(input("enter number: "))
    num2 = int(input("enter another number: "))
    print(num1 > num2)

def isBigger():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    num3 = int(input("enter third number: "))
    print(num1 > num2 or num1 > num3)

def isBiggest():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    num3 = int(input("enter third number: "))
    print(num1 > num2 and num1 > num3)