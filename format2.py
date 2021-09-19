given_name = "Peter"
family_name = "Capaldi"
occupation = "Timelord"
print("Name: {0} {1} \nOccupation: {2}".format(given_name, family_name, occupation))
print("Name: {0} {1} \nOccupation: {2}".format(given_name, family_name, occupation))

print()
print("=============================")
factor = 5
for number in range(1, 6):
    answer = number*factor
    print(number, factor, sep='*', end=' ')
    print("= ", answer)

print()
print("=============================")
given_Name = input("Enter your first name ")
family_Name = input("Enter your surname ")
occupation = input("What is your job? ")
home = input("Where were you born? ")
print("New style Formatting")
print("Name: {0} {1} \tOccupation: {2} \tPlace of Birth: {3} \n".format(given_Name, family_Name, occupation, home))