class Person(object):
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):
    def __init__(self,name):
        super().__init__(name)
    def isEmployee(self):
        return True

emp = Person('Musleh')
print(emp.getName(),emp.isEmployee())

emp = Employee('Khan')
print(emp.getName(),emp.isEmployee())

# issubclass(subclass,superclass) - True

# multiple inheritance
class Base1(object):
    def __init__(self):
        self.str1 = 'Md'
        print('Base1')

class Base2(object):
    def __init__(self):
        self.str2 = 'Musleh'
        print('Base2')

class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1,self.str2)
ob = Derived()
ob.printStrs()

# Access parent members in a subclass
# using Parent class name

class Base(object):
    def __init__(self,x):
        self.x = x

    def __repr__(self):
        return "%d"%(self.x)

class Derived(Base):
    def __init__(self,x,y):
        Base.x = x
        self.y = y

    def printXY(self):
        print(Base.x, self.y)

# Driver Code
d = Derived(10,20)
d.printXY()

b = Base(100)
print(b)

# using super()
class Base(object):
    def __init__(self,x):
        self.x = x

class Derived(Base):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y
    def printXY(self):
        print(self.x,self.y)

d = Derived(10,20)
d.printXY()

# super(Employee,self).__init__(name)