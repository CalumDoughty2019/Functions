def sum_of_two_numbers(x, y):
    return x + y

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

def higher_than(x, y):
    if x < y:
        return True
    else:
        return False

first_num = int(input("Enter a whole number: "))
second_num = int(input("Enter another whole number: "))
answer = sum_of_two_numbers(first_num, second_num)
print("The answer is ", answer)

answer2 = absolute_value(answer)
print("The absolute answer is ", answer2)

answer3 = higher_than(answer, answer2)
print("Is the first answer higher than the second? ", answer3)
