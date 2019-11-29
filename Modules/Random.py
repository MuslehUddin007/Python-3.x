import random

print("A random number from list is : ",end="")
print(random.choice([1,4,8,10,3]))

print("A random number from range is : ",end="")
print(random.randrange(20,50,3))

li = [1,4,5,10,2]
print("The list after shuffling is : ",end="")
random.shuffle(li)
for i in li:
    print(i,end=" ")

