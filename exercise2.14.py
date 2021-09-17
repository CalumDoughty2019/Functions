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
    #1
    print("turn_clockwise")
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    #2
    print("day_name")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    #3
    print("day_num")
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    #4
    print("day_add")
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    #5
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    #6
    print("days_in_month")
    test(days_in_month("February") == 28)
    #print(days_in_month("February"))
    test(days_in_month("December") == 31)
    #7
    print("to_secs")
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    #8
    test(to_secs(2.5, 0, 10.71) == 9010)
    #print(to_secs(2.5, 0, 10.71))
    test(to_secs(2.433, 0, 0) == 8758)
    #print(to_secs(2.433, 0, 0))
    #9
    print("hours/minutes/seconds_in")
    test(hours_in(9010) == 2)
    #print(hours_in(9010))
    test(minutes_in(9010) == 30)
    #print(minutes_in(9010))
    test(seconds_in(9010) == 10)
    #10
    print("modulo")
    test(3 % 4 == 0)
    test(3 % 4 == 3)
    test(3 / 4 == 0)
    test(3 // 4 == 0)
    test(3 + 4 * 2 == 14)
    test(4 - 2 + 2 == 0)
    test(len("hello, world!") == 13)
    #11
    print("compare")
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    #12
    print("hypotenuse")
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    #13
    print("slope & intercept")
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    #14
    print("is_even")
    test(is_even(68) == True)
    test(is_even(47) == False)
    #15
    print("is_odd")
    test(is_odd(68) == False)
    test(is_odd(47) == True)
    #16
    print("is_factor")
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    #17
    print("is_multiple")
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    #18
    print("f2c")
    test(f2c(212) == 100)  # Boiling point of water
    test(f2c(32) == 0)  # Freezing point of water
    test(f2c(-40) == -40)  # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)
    #19
    print("c2f")
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)




#1
def turn_clockwise(direction):
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"
    else:
        #print("Please choose N, E, S, or W")
        return None

#2
def day_name(number):
    if number == 0:
        return "Sunday"
    elif number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    elif number == 6:
        return "Saturday"
    else:
        return None

#3
def day_num(day):
    if day == "Sunday":
        return 0
    elif day == "Monday":
        return 1
    elif day == "Tuesday":
        return 2
    elif day == "Wednesday":
        return 3
    elif day == "Thursday":
        return 4
    elif day == "Friday":
        return 5
    elif day == "Saturday":
        return 6
    else:
        return None

#4
def day_add(day, leaving):
    getNumberForDay = day_num(day)
    newNumber = (getNumberForDay + leaving) % 7
    getDayForNumber = day_name(newNumber)
    return getDayForNumber

#5
#Already works because "getNumberForDay + leaving" would still minus a minus "leaving" variable
#and the modulus treats negatives as if they are positive

#6
def days_in_month(month):
    if month == "February":
        return 28
    elif month == "January" or "March" or "May" or "July" or "August" or "October" or "December":
        return 31
    elif month == "April" or "June" or "September" or "November":
        return 30
    elif month == "February":
        return 28
    else:
        return None

#7 & #8
def to_secs(hours, minutes, seconds):
    minutesInHours = hours * 60
    minutes = minutesInHours + minutes
    secondsInMinutes = minutes * 60
    seconds = math.floor(secondsInMinutes + seconds)
    return seconds

#9
def hours_in(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    return math.floor(hours)
    #would be better to do minutes_in first as then I can use that function to solve this one

def minutes_in(seconds):
    minutes = seconds / 60
    actualMinutes = minutes % 60
    return math.floor(actualMinutes)

def seconds_in(seconds):
    seconds = seconds % 60
    return seconds

#10
#test(3 % 4 == 0) fails because modulo collects remainder so remainder is 3
#test(3 / 4 == 0) fails because its 0.75
#test(3+4  *  2 == 14) fails because BODMAS. Answer is 11
#test(4-2+2 == 0) fails because apparently not BODMAS. Apparently python has subtraction come first

#11
def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

#12
def hypotenuse(a, b):
    ab = (a**2) + (b**2)
    c = math.sqrt(ab)
    return c

#13
def slope(x1, y1, x2, y2):
    m = ((y2-y1)/(x2-x1))
    return m

def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    yintercept = y1 - (m * x1)
    return yintercept

#14
def is_even(n):
    if n % 2 == 1:
        return False #odd
    else:
        return True #even

#15
def is_odd(n):
    if is_even(n):
        return False
    else:
        return True

#16
def is_factor(f, n):
    if n % f == 0:
        return True
    else:
        return False

#17
def is_multiple(f, n):
    if is_factor(n, f) == True:
        return True
    else:
        return False

#18
def f2c(fahrenheit):
    celsius = round((fahrenheit - 32) / 1.8)
    return celsius

#19
#https://www.pythoncentral.io/use-python-convert-fahrenheit-celsius/
def c2f(celsius):
    fahrenheit = round((celsius * 1.8) + 32)
    return fahrenheit


test_suite() #driver for testing
