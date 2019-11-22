pyString = 'Python'
print(sorted(pyString))

print(sorted(pyString,reverse=True))

#sort the list using sorted having a key function
def takeSecond(elem):
    return elem[1]

#random list
random = [(2,2),(3,4),(4,1),(1,3)]
sortedList = sorted(random,key=takeSecond)
print('Sorted List : ', sortedList)