greeting = "Hello, world!"
print(greeting)

greeting = "Yello, world!"
print(greeting)

#strings are immutable, so we cannot assign a new letter value to string index
#greeting[0] = "H"
#print(greeting)

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:] #we create a new string and carry everything except swap that single character
print(newGreeting)