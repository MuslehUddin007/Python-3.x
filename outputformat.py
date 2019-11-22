print("First : %2s, Second : %2d, Third : %2.2f"%('Musleh',12,45.3445))
# %o --for octal
#%E --for exponential value

print("First : {0} , Second : {1} , Third : {other}".format('Musleh','Uddin',other='Khan'))

print("First : {0:2d}, Second : {1:6.2f}".format(12,23.345))

tab = {'geeks':12, 'for': 13, 'geek':14}
print("Geeks: {0[geeks]:d}, {0[for]:d}, {0[geek]:d}".format(tab))

data = dict(fun = "GeeksForGeeks", adj="Portal")
print("I love {fun} computer {adj}".format(**data))


cstr = "Md Musleh Uddin"
print(cstr.center(40,'#'))
print(cstr.ljust(40,'-'))
print(cstr.rjust(40,'$'))


str = "|{0:<10}|{1:^10}|{2:>10}".format('Md','Musleh','Uddin')
print(str)

str1 = 'Md'
str2 = 'Musleh'

#repr is used to print the string along with the quotes
print(repr(str1 and str2))
print(repr(str1 or str2))
print(repr(not str1))

"""
%d --Integer
%f --float
%s --string
%x --hexadecimal
%o --octal
"""

#string template
from string import Template

t = Template('x is $x')
print(t.substitute({'x':1}))

student = [('Musleh',90),('Ashik',80),('Jemi',85)]
t = Template("Hi $name, you have got $marks marks")
for i in student:
    print(t.substitute(name = i[0], marks = i[1]))

#regexp is the delimiting regular expression;
#limit is limit the number of splites to be make
# str.split(regexp="",limit = string.count(str))

def my_function():
    """Demonstrate docstrings and does nothing really."""

print(my_function.__doc__)
help(my_function)


class complexnumber():
    """This is from class"""
    def __init__(self):
        """This is from init function"""
    def add(self,num):
        """This is from add function"""



help(complexnumber)
help(complexnumber.add)

