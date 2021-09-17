userName = "Barney Rubble"
def set_name():
    global userName
    userName = input("Enter your name: ")
    #return userName      ##this will use local

def print_name():
    print("The user of this program is: " + userName)

set_name()
print_name()