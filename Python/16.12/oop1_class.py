print("into oop_class.py ")
'''
what is class?
what is object?
what is properties? ( vs variable) 
'''


# create class Box
class Box:
    print('this code run!!!')
    width = 100
    height = 200

print('***************')
box1 = Box()
print(type(box1))  # <class '__main__.Box'>

print(box1.width)  # 100
box1.width = 150
print(box1.width)  # 150



# create object form class
# after we can change the objects..



# create class Person
class Person:
    first = 'Israel'
    last = 'Israeli'
    age = 0


# create objects form class
p1 = Person()
print(p1.first, p1.last)  # Israel Israeli

# after we can change the object and override properties..
p1.first = "Gal"
print(p1.first, p1.last)  # 'Gal Israeli'

# we can change the etch objects and override properties for specific object..
p2 = Person()
p2.first = "Dana"
print(p2.first, p2.last)  # Dana Israeli

