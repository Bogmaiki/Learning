print("into lists.py ")
'''

List is ordered, changeable collection (allow duplicate values)

create - YES - list1 = ["Gal",10]
get    - YES - x = list1[0]
search - YES - .index(v)
add    - YES - use append(v) to add one value 
set    - YES - list1[0] = x
remove - YES - use .pop(k) / .remove(v)
join   - YES - use .extend() / list3 = list1 + list2
loop   - YES - for i in list1:

'''

# create
list1 = []
print(type(list1))  # <class 'list'>

print("********** Example **********")
names = ["Gal", "Ben", "Ran", "Yam"]  # create
print(names)
print(len(names))  # 4

x = names[1]  # get
print(x) # 'Ben'

names[1] = "Ram"  # set
print(names)


names[2:4] = ["Dan","Ron"] # delete key 2+3 and add "Dan" and "Tal"
print(names[2:4]) # ['Dan', 'Ron']


names.append("Tal")  #add

print(names)

del names[2]  # delete
print(names)

y = "Gal" in names  # search
print(y)  # True

print("********** Example  **********")
for name in names:  # loop
    print(name)




print("********** Example **********")
user = ["Gal", 'Lavi', 32, True, False, True]
print(user)
print(user[0])
print(user[1])
print(type(user[2]))

# len() of
x = len(user)
print(x)







