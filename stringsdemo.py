fruit = "banana"
letter = fruit[1]
print(letter)

letter = fruit[0]
print(letter)
print("There are ", len(fruit), "characters in", fruit)

length_of_fruit = len(fruit)
last_letter = fruit[length_of_fruit-1] #need -1 as index starts at 0, so crash will be caused by value at index 6 if we dont minus 1
smarter_last_letter = fruit[-1]
print("Last letter is", smarter_last_letter)