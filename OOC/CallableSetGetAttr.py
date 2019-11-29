x = 5

def testFunction():
    print('Test')

y = testFunction

if(callable(x)):
    print('x is callable')
else:
    print('x is not callable')

if(callable(y)):
    print('y is callable : ',y.__qualname__)
else:
    print('y is not callable') 


# callable when used in OOP
class Foo1:
    name = 'Md Musleh Uddin'
    def __call__(self):
        print('Print Something')

print(callable(Foo1))

#getattr()
foo = Foo1()
print('The getattr : ',getattr(foo,"name"))
print('Another method : ',foo.name)

# setattr()
setattr(foo,"name","Md Mujahid Uddin Khan")
print("After modification : ",getattr(foo,"name"))

# hasattr()
print("Person has name ? ",hasattr(foo,"name"))