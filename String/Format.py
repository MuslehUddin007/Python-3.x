#Format() method

#default arguments
print("Hello {}, your balance is {}.".format("Musleh",180.234))

#positional arguments
print("Hello {0}, your balance is {1}.".format("Musleh",180.235))

#keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Musleh",blc=180.234))

#mixed arguments
print("Hello {0}, your balance is {blc}.".format("Musleh",blc=180.234))

#integer, float, octal, binary and hex arguments
print("Integer: {0:d}, Float: {0:f}, Binary: {0:b}, Octal: {0:o}, Hexadecimal: {0:x}".format(12))


#numbers with minimux width
print("{:5d}, {:8.3f}".format(12,15.1234))
print("{:05d}, {:08.3f}".format(12,15.1234))

#show the + and - sign
print("{:+f} {:+f}".format(12.23,-12.23))

#print with left,right,center alignment
print("{0:<d} {0:^d} {0:>d}".format(12))

#string padding
print("{:*^5}".format("cat"))

print("{:.3}".format("caterpillar"))

#define Person class
class Person:
    age = 20
    name = "Musleh"

#format name and age
print("{p.name}'s age is : {p.age}.".format(p = Person()))

#define Person dictionary
person = {'age': 23, 'name': 'Musleh'}
print("{p[name]}'s age is : {p[age]}".format(p=person))

#easier way
print("{name}'s age is : {age}.".format(**person))

#dynamic formatting
str = "{:{fill}{align}{width}}"
print(str.format('cat',fill='*',align='^',width=5))

num = "{:{align}{width}.{precision}f}"
print(num.format(123.345,align='<',width=8,percision=2))

import datetime
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

#complex number
complexNumber = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))

#custom_format
class people:
    def __format__(self,format):
        if(format == 'age'):
            return '23'
        return 'None'

print("Musleh's age is : {:age}".format(Person()))

#str and repr
print("Quotes: {0!r}, Without Quotes: {0!s}".format("cat"))

class Per:
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"

print("repr: {p!r}, str: {p!s}".format(p = Per()))


