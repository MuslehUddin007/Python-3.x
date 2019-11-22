# pass multiple value
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Md','Musleh','Uddin','Khan')

def myFun(arg1,*argv):
    print('First argument : ',arg1)
    for arg in argv:
        print('Next argument through *argv : ',arg)

myFun('Md','Musleh','Uddin','Khan')

# key worded argument
def myFun(**kwargs):
    for key,value in kwargs.items():
        print('%s == %s'%(key,value))

myFun(first='Md',second='Musleh',third='Uddin')

# use *args and **kwargs together
def myFun(arg1,arg2,arg3):
    print('arg1 : ',arg1)
    print('arg2 : ',arg2)
    print('arg3 : ',arg3)

args = ('Md','Musleh','Uddin')
myFun(*args)

kwargs = {'arg1':'Md','arg2':'Musleh','arg3':'Uddin'}
myFun(**kwargs)