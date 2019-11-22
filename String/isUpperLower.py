def check(str):
    if str.islower():
        print("Lower")
    elif str.isupper():
        print("Upper")
    else:
        print("With Upper and Lower")


check("musleh")
check("Musleh")
check("MUSLEH")
