class MyClass:
    #hidden member of MyClass
    __hiddenVariable = 0
    def add(self,increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)

#Driver code
myObject = MyClass()
myObject.add(2)
myObject.add(5)

#this line cause erro (accessing hidden member)
#print(myObject.__hiddenVariable)

# access hidden member by a tricky syntam
print(myObject._MyClass__hiddenVariable)