def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items

    return sum(args) + total


print(super_func(1, 2, 3, 4, num1=10, num2=5, num3=20))
