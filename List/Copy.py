import copy

list1 = [1,2,3,4,5]
list2 = list1.copy()

list1.pop()
print(list2)
print(list1)

# shallow copy 
list3 = copy.copy(list1)
list3 = list1[:]

# deep copy
list2 = list1
list3 = copy.deepcopy(list1)