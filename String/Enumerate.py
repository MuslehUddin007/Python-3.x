""" The enumerate() method adds counter to an iterable and returns it """

grocery = ['bread','milk','butter']
enumerateGrocery = enumerate(grocery)
print(list(enumerateGrocery))

enumGrocery = enumerate(grocery,10)
print(list(enumGrocery))

for item in enumerate(grocery):
    print(item)

print('\n')
for count,item in enumerate(grocery):
    print(count,item)

print('\n')
for count,item in enumerate(grocery,100):
    print(count,item)
