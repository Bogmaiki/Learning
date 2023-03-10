
cities1 = ['Tel-Aviv', 'Jerusalem', 'Ashdod', 'Bat-yam', 'Ramat-Gan']
print(cities1)


# append - gat value >> add value to end of list
cities1.append('Holon')
print(cities1)


# index - get value >> return the first key (Error if the value not in list)
x = cities1.index("Ashdod")
print(x)


# pop - get key in list >> remove the value ( return the value )
x = cities1.pop(1)
print(x)
print(cities1)


# pop -  without value remove the last key in list
x = cities1.pop()
print(x)
print(cities1)


# remove -  get value >> remove the first key in list
cities1.remove("Ashdod")
print(x)
print(cities1)


# insert -  get key and value >> add key and value to list
cities1.insert(1, "Arad")
print(cities1)


# count - gat value >> return number of items the value in list
cities1.append("Ramat-Gan")
print(cities1)
x = cities1.count("Ramat-Gan")
print(x)


# sort -  sort the list a-z (for z-a >> use reverse=True parameter )
cities1.sort()
print(cities1)
cities1.sort(reverse=True)
print(cities1)

# extend - get list,dict, set, tuple >> add to end of list
cities2 = ["Haifa", "Beer-Sheva"]
cities1.extend(cities2)
print(cities1)


# clear - clear all the items in list
cities1.clear()
print(cities1)


