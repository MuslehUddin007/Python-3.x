""" The __del__() function is known as destructors """
class Employee:
    # constructor
    def __init__(self):
        print('Constructor called, Employee created.')
    # destructor
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
#del obj
print('Program End.........')

