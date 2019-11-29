from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('Full name of this method: ',func.__qualname__)
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls

@debugmethods
class Calc:
    def add(self,x,y):
        return x+y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y

mycal = Calc()
print(mycal.add(2,3))
print(mycal.mul(5,2))