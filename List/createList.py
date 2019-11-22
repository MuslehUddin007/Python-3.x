""" List are mutable elements """

List = [84,'Musleh',3.67]
print(List[1])

# add elements on list
# append only works addition of elements at the end of the list
List.append('Khan')

#using iterator
for i in range(1,4):
    List.append(i)

print(List)

#Insert add elements at the desired position
List.insert(0,'Md')
print(List)

# extend used to add multiple elements at the end
List.extend([5,'Akil','programmer'])
print(List)

# remove method only removes one elements at a time
List.remove(5)
for i in range(1,4):
    List.remove(i)

print(List)

# pop method remove last element of the list
List.pop()
List.pop(2)
print(List)

# reverse list
reverseList = List[::-1]
print(reverseList)

# delete elements in range
del List[1:3]
print(List)

#sort list
lis = [1,4,6,3,7,9,6,10,2]
lis.sort()
lis.reverse()
print(lis)

# remove all elements from the list
lis.clear()
print(lis)
