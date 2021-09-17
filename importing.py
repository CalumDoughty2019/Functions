import math
total = 0
for count in range(1, 6):
    new_number = int(input("Enter a number: "))
    total = total + new_number
average = total / count
#print("The average is: ", average)

averageUp = math.ceil(average) #ceiling rounds up
averageDown = math.floor(average) #floor rounds down
squareRoot = math.sqrt(average) #gets the square root

print("The average is: ", average, "\n")
print("The ceiling is: ", averageUp, "\n")
print("The floor is: ", averageDown, "\n")
print("The square root is: ", squareRoot, "\n")