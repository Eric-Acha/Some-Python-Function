# start by filtering the evens into a list
# then check and return the highest even
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([7, 12, 9, 10, 4, 2, 14, 23, 6]))
