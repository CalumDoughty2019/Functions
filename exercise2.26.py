import sys
import math

### TEST FUNCTION
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

### TEST SUITE
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    #7
    print()
    print("reverse")
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
    #8
    print()
    print("mirror")
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")
    #9
    print()
    print("remove_letter")
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")
    #10
    print()
    print("is_palindrome")
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(not is_palindrome(""))    # Is an empty string a palindrome?
    #11
    print()
    print("count")
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)
    #12
    print()
    print("remove")
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")
    #13
    print()
    print("remove_all")
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")



#1
#"Python"[1] = 'y'
#"Strings are sequences of characters."[5] = 'g'
#len("wonderful") = 9
#"Mystery"[:4] = 'Myst'
#"p" in "Pineapple" = True
#"apple" in "Pineapple" = True
#"pear" not in "Pineapple" = True
#"apple" > "pineapple" = False
#"pineapple" < "Peach" = False

#2
print()
print("suffixes")
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

#3
print()
print("count_letters")
def count_letters(string_input, letter_input):
    count = 0
    for char in string_input:
        if char == letter_input:
            count += 1
    return count

print(count_letters("banana", "a"))

#4
print()
print("better_count_letters")
def better_count_letters(string_input, letter_input):
    global length
    length = 0
    new_string_input = string_input
    count = 0
    length = len(string_input)
    for i in range(1, length):
        if(new_string_input == ""):
            break
        elif str.find(new_string_input, letter_input):
            location = str.find(new_string_input, letter_input) +1
            new_string_input = new_string_input[location:]
            length = len(new_string_input)
            count += 1
    return count

print(better_count_letters("banana", "a"))

#5
print()
print("Wilde")
wilde = "We are all in the gutter, but some of us are looking at the stars."
count = 0
for i in range(1, len(wilde)):
    if str.find(wilde, ","):
        wilde = wilde.replace(",", "")
    if str.find(wilde, "."):
        wilde = wilde.replace(".", "")
list = wilde.split()
size = len(list)
for j in range(1, size):
    if str.find(list[j], 'e'):
        count += 1
percent = (count/size)*100
print("Your text contains " + str(size) + " words, of which " + str(count) + " ({0:.2f}%) contain an \"e\".".format(percent))

#6
print()
print("Multiplication Table")
print("\t\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12")
print(" :----------------------------------------------------")
for i in range(1, 13):
    print(str(i) + ":\t\t", end="")
    for j in range(1, 13):
        if j == 12:
            print(str(i * j))
        else:
            print(str(i*j), end="\t")

#7
def reverse(word_to_reverse):
    reversed = word_to_reverse[::-1]
    return reversed
    #print(reversed)

#8
def mirror(word_to_mirror):
    mirrored = reverse(word_to_mirror)
    joinedMirror = word_to_mirror + mirrored
    return joinedMirror

#9
def remove_letter(letter, word):
    word = word.replace(letter, "")
    return word

#10
def is_palindrome(check_word):
    reversed = reverse(check_word)
    if check_word == "":
        return False
    elif check_word == reversed:
        return True
    else:
        return False

#11
def count(piece, word):
    #return word.count(piece)

    # return len(word.findall('(?==' + piece + ')', ''+word+''))
    # print(len(word.findall('(?==' + piece + ')', ''+word+'')))

    len1 = len(word)
    len2 = len(piece)
    j =0
    counter = 0
    while(j < len1):
        if(word[j] == piece[0]):
            if(word[j:j+len2] == piece):
                counter += 1
        j += 1

    return counter

    # global length
    # length = 0
    # new_string_input = word
    # count = 0
    # length = len(word)
    # for i in range(1, length):
    #     if (new_string_input == ""):
    #         break
    #     elif str.find(new_string_input, piece):
    #         location = str.find(new_string_input, piece) + 1
    #         if location == 0:
    #             return count
    #         new_string_input = new_string_input[location:]
    #         length = len(new_string_input)
    #         count += 1
    # return count

#12
def remove(piece, word):
    removed = word.replace(piece, "", 1)
    return removed

#13
def remove_all(piece, word):
    removed = word.replace(piece, "")
    return removed


test_suite() #driver for testing
