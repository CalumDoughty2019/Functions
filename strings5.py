import string

fruit = "banana"
index = str.find(fruit, "a")
print(index)

print(str.find("banana", "na"))
print(str.find("banana", "na", 3))
print(str.find("bob", "b", 1, 2)) #when -1 is returned it means that nothing was found
print(str.find("bbo", "b", 1, -1))