"""
Note: Keys in a dictionary doesn't allows Polymorphism
Keys of dictionary must be unique and of immutable data type such as Strngs, Intergers and Tuples.
"""

Dict = {1:'Md',2:'Musleh',3:'Uddin',4:'Khan'}
print("Dictionary with the use of Integer keys: ")
print(Dict)

# create dictionary with pait item
Dict = dict([(1,'Geeks'),(2,'For')])
print(Dict)

# adding elements on dictionary
Dict[3] = 'Musleh'
Dict['Uddin']= 4
print(Dict) 

# accessing elements on dictionary
print('Accessing elements using key: ')
print(Dict[3])

# accessing elements using get method
print(Dict.get(3))

# removing elements from dictionary
del Dict['Uddin']
Dict.pop(1)
# popitem
#clear
