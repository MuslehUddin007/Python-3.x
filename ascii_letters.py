import string

def check(value):
    for letter in value:
        if letter not in string.ascii_letters:
            return False
    return True

input1 = "MdMuslehUddinKhan"
print(input1," --> ",check(input1))

input2 = "Md Musleh Uddin Khan"
print(input2," --> ", check(input2))

input3 = "Md_Musleh_Uddin_Khan"
print(input3, "--> ",check(input3))
