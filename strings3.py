import sys

word = input("Enter the name of a fruit: ")
fruit = "blackberry"
if word == fruit:
    print("Good guess!")
else:
    print("although we like", word, ", you guessed wrong")

#sys.exit(0)

if word < "banana":
    print("Your word," + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")