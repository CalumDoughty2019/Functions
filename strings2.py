import sys

fruit = "Blackberry"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print("\t", letter, end=" ")
    index = index + 1
print()

for char in fruit:
    print("\t", char, end=" ")
print()

#sys.exit(0)

count = 0
for char in fruit:
    selected = "a"
    if char == selected:
        count = count + 1
print("The character", selected, "appears", count, "times in", fruit)

# sys.exit(0)

s = "Peter, Paul, and Mary"
print("Zero to 5 = ", s[0:5])
print("7 to 11 = ", s[7:11])
print("17 to 21 = ", s[17:21])
print("The first three characters in", fruit, "are", fruit[:3])
print("The last three characters in", fruit, "are", fruit[3:]) #gives incorrect, this does everything but first three letters. Needs to be a minus.
print("The last three characters in", fruit, "are", fruit[-3:])