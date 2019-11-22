class A:
    def __init__(self,a):
        self.a = a

    #adding two objects
    def __add__(self,o):
        return self.a + o.a

ob1 = A(1)
ob2 = A(2)
ob3 = A('Geeks')
ob4 = A('For')
print(ob1+ob2)
print(ob3+ob4)

# complex
class complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,other):
        return self.a + other.a, self.b + other.b

    def __str__(self):
        return self.a, self.b

ob1 = complex(1,2)
ob2 = complex(2,3)
ob3 = ob1 + ob2
print(ob3)

# comparison operators
class A:
    def __init__(self,a):
        self.a = a

    def __gt__(self,other):
        if(self.a > other.a):
            return True
        else:
            return False

ob1 = A(2)
ob2 = A(3)
if (ob1 > ob2):
    print('Ob1 is greater then ob2')
else:
    print('Ob2 is greater then  ob1')

# equality and less then operator
class A:
    def __init__(self,a):
        self.a = a

    def __lt__(self,other):
        if(self.a < other.a):
            return 'Ob1 is less than ob2'
        else:
            return 'ob2 is less than ob1'

    def __eq__(self,other):
        if(self.a == other.a):
            return 'Both are euqla'
        else:
            return 'Not equal'

ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob4 == ob3)


"""
Binary Operators:
 __add__ (+)
 __sub__ (-)
 __mul__ (*)
 __truediv__ (/)
 __floordiv__ (//)
 __mod__ (%)
 __pow__ (**)
Comparison Operators:
 __lt__ (<)
 __gt__ (>)
 __le__ (<=)
 __ge__ (>=)
 __eq__ (==)
 __ne__ (!=)
Assignment operators:
 __isub__ (-=)
 __iadd__ (+=)
 __imul__ (*=)
 __idiv__ (/=)
 __ifloordiv__ (//=)
 __imod__ (%=)
 __ipow__ (*=)
Unary Operators:
 __neg__ (-)
 __pos__ (+)
 __invert__ (~)
 
"""