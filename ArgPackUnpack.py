# list pack unpack
def fun(a,b,c,d):
    print(a,b,c,d)

my_list = [1,2,3,4]
fun(*my_list)

# another
args = [1,5]
print(range(*args))

# packing
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum

print(mySum(1,2,3,4,5))
print(mySum(10,20))

# unpacking dictionary
d = {'a':1,'b':2,'c':3,'d':4}
fun(**d)

#packing
def fun(**kwargs):
    print(type(kwargs))

    for key in kwargs:
        print("%s = %s" % (key,kwargs[key]))

#driver code
fun(name='geeks',id='101',language='Python')