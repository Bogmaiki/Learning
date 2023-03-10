# EX 1
people = ["Avi", "Moshe", "Yosi", "Daniel", "Mark"]
print(people)
print(type(people))
print(len(people))
x = people[2]
print(x)
x = people[0:2]
print(x)
people[1] = "Gal"
print(people[1])
people[2:4] = ["Leon", "Oren"]
print(people)
people.append("Moshe")
print(people)
del people[1]
print(people)
for i in people:
    print(i)

# EX 2
print("****************************************")
fruits = ["banana", "watermelon", "apple", "avocado", "mango", "orange", "peach"]
print(fruits)
print(type(fruits))
print(len(fruits))
x = fruits[3]
print(x)
x = fruits[2:5]
print(x)
fruits[5] = "pear"
print(fruits)
fruits[2:5] = ["grape", "papaya", "cherry"]
print(fruits)
fruits.append("apple")
print(fruits)
del fruits[2]
print(fruits)
for i in fruits:
    print(i)

# EX 3
print("*************************************************")
