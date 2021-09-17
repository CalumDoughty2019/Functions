import math

### ADD
def add():
    first = int(input("Please input first number: "))
    second = int(input("Please input second number: "))
    answer = first + second
    print("Answer = " + str(answer))

### SUBTRACT
def subtract():
    first = int(input("Please input first number: "))
    second = int(input("Please input second number: "))
    answer = first - second
    print("Answer = " + str(answer))

### MULTIPLY
def multiply():
    first = int(input("Please input first number: "))
    second = int(input("Please input second number: "))
    answer = first * second
    print("Answer = " + str(answer))

### DIVIDE
def divide():
    first = int(input("Please input first number: "))
    second = int(input("Please input second number: "))
    answer = first / second
    print("Answer = " + str(answer))

### SQUAREROOT
def squareroot():
    first = int(input("Please input a number: "))
    answer = math.sqrt(first)  # gets the square root
    print("Answer = " + str(answer))

### VOLUME
def volume():
    radius = int(input("Please input the RADIUS in metres: "))
    height = int(input("Please input the HEIGHT in metres: "))
    answer = math.pi * ((radius*radius) * height)
    print("Answer = " + str(answer) + "m^3")

### WALLPAPER PROBLEM
def wallpaper():
    print("ROOM")
    height = int(input("Please input the HEIGHT in metres: "))
    length = int(input("Please input the LENGTH in metres: "))
    width = int(input("Please input the WIDTH in metres: "))
    opp1 = 2 * (height * length) #finds the metres squared of 2 opposite walls
    opp2 = 2 * (height * width) #finds the metres squared of the other walls
    total = opp1 + opp2
    print("DOORS/WINDOWS")
    numbers = int(input("How many doors/windows do you have in this room?: "))
    j = 0
    for i in range(numbers):
        j += 1
        print("area" + str(j))
        heighty = int(input("Please input the HEIGHT in metres: "))
        widthy = int(input("Please input the WIDTH in metres: "))
        gaps = heighty * widthy
        total -= gaps
    print("\n")
    print("Surface area to cover = " + str(total) + "m^2")
    paper = math.ceil(total / 5)
    print("Wallpaper needed = " + str(paper) + " rolls")

### COMPOUND
#https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
#https://www.geeksforgeeks.org/python-program-for-compound-interest/
def compound():
    principal = float(input("Initial investment sum: "))
    term = float(input("Term time (in yrs): "))
    interestRate = float(input("Interest rate: "))

    #temp = (1 + (interestRate/1))**term
    finalAmount = principal * (pow((1 + interestRate/100), term))
    print("Principal sum = " + str(round(principal, 2)))
    compoundInterest = finalAmount - principal
    print("Interest accumulated = " + str(round(compoundInterest, 2)))
    print("Balance Total = " + str(round(finalAmount, 2)))






############################# MENU
checker = 0
while checker == 0:
    checker = 0
    print("Arithmetic Demo")
    print("================")
    print("1. Add two numbers")
    print("2. Subtract one number from another")
    print("3. Multiply two numbers together")
    print("4. Divide one number by another")
    print("5. Find the square root of a number")
    print("6. Exit")
    print("7. Calculate volume of cylindrical fuel tank")
    print("8. Wallpaper problem")
    print("9. Compound interest")
    print("\n")
    print("Please make your choice:")
    choice = int(input(">>> "))
    if choice == 1:
        #checker = 1
        add()
        print("\n")
        input("Press Enter to continue...")
        print("\n")
        continue
    elif choice == 2:
        #checker = 1
        subtract()
        print("\n")
        input("Press Enter to continue...")
        print("\n")
        continue
    elif choice == 3:
        #checker = 1
        multiply()
        print("\n")
        input("Press Enter to continue...")
        print("\n")
        continue
    elif choice == 4:
        #checker = 1
        divide()
        print("\n")
        input("Press Enter to continue...")
        print("\n")
        continue
    elif choice == 5:
        #checker = 1
        squareroot()
        print("\n")
        input("Press Enter to continue...")
        print("\n")
        continue
    elif choice == 6:
        quit()
    elif choice == 7:
        #checker = 1
        volume()
        print("\n")
        input("Press Enter to continue...")
        print("\n")
        continue
    elif choice == 8:
        #checker = 1
        wallpaper()
        print("\n")
        input("Press Enter to continue...")
        print("\n")
        continue
    elif choice == 9:
        #checker = 1
        compound()
        print("\n")
        input("Press Enter to continue...")
        print("\n")
        continue
    else:
        print("Please choose a valid menu option")
        print("\n")