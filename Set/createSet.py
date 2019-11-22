""" Set is mutable and has no duplicate elements and an unordered collection """

set1 = set(['Geeks','For','Geeks'])
print(set1)

# unique item only
set2 = set([1,2,3,3,4,4,5,6,1])
print(set2)

# adding elements
set2.add(8)
set2.add(9)

# adding elements using iterator
for i in range(10,14):
    set2.add(i)

print('Set2 Elements: ',set2)

# update method to add two or more elements 
set1.update([10,11])
print('Set1 elements: ',set1)

# accessing elements using for loop
for i in set1:
    print(i,end=" ")

# using in keyword
print('\n')
print("Geeks" in set1)

# removing elements
set1.remove(10)
set1.remove(11)

# pop function -Better not use in set
set2.pop()

# to remove all elements 
set2.clear()