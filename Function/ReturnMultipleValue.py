# using object
class Test:
    def __init__(self):
        self.str = 'Md Musleh Uddin'
        self.x = 20

t = Test()
print(t.str)
print(t.x)

# Using Tuple
def fun():
    str = 'Md Musleh Uddin'
    age = 20
    return str,age;

str,age = fun()
print(str,age)

# Using List
def fun():
    str = 'Md Musleh Uddin'
    age = 20
    return [str,age]

list = fun()
print(list)

# Using Dictionary
def fun():
    d = dict()
    d['str'] = 'Md Musleh Uddin'
    d['age'] = 20
    return d

d = fun()
print(d)