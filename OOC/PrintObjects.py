class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a:%s b:%s"%(self.a,self.b)

    def __str__(self):
        return "From str method of Test : a is %s,"\
            "b is %s" % (self.a,self.b)

#Driver Code
t = Test(1234,5678)
print(t) #__str__()
print([t]) #__repr__()
# if no __str__() method is define only __repr__() then print(t)