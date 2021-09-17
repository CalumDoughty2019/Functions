def print_twice(something):
    print(something, something)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
    print("The value of cat is: ", cat)


phrase1 = "A big boy did it "
phrase2 = "and ran away"

cat_twice(phrase1, phrase2)
#print("The value of cat is: ", cat)