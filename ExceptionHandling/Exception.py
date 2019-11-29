a = [1,2,3]

try:
    print("Second element = %d " %(a[1]))
    print("Fourth element = %d " %(a[3]))
except IndexError:
    print("An error occured")

try:
    a = 3
    if a < 4:
        b = a/(a-3)
    print("Value of b = ", b)
except (ZeroDivisionError, NameError):
    print("\nError Occured and Handled")

def abc(a,b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("A/b result in 0")
    else:
        print(c)

abc(2.0,3.0)
abc(3.0,3.0)

try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise