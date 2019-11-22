from functools import *

#normal function
def add(a,b,c):
    return 100*a + 10*b + c

#A partial function
add_part = partial(add,c=2,b=1)


#calling partial function
print(add_part(3))