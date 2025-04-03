# Test if old enough to drive

def can_drive():

    name = input("enter name: ")
    age = int(input("enter age: "))
    license_satus = True

    if age > 18 and license_satus:
        print(f"Welcome {name}, you are good to go!.")
    elif age == 18 and license_satus:
        print(f"Hello {name}, you can drive with a qulified adult.")
    else:
        print(f"{name}, you are not qualified to drive.")


can_drive()
