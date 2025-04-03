def multiply(num1, num2):
    return (num1 * num2)

# updated function to take any num of arguments and sum them up
# In case you need to add more than two nums


def addition(*args):
    return sum(args)


def subtraction(num1, num2):
    return num1 - num2


def division(num1, num2):
    return num1/num2


def square(num):
    return num * num


print(addition(1, 3, 4, 5))
