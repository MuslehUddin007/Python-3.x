import functools
import operator
import itertools

lis = [1,2,3,4,5]
print("The sum of the list elements is : ",end="")
print(functools.reduce(lambda a,b: a+b, lis))

print("The maximum element of the list is : ",end="")
print(functools.reduce(lambda a,b: a if a > b else b, lis))

# using operator
print("The multiply of the list is : ",end="")
print(functools.reduce(operator.mul,lis))

print("Concatenated String : ",end="")
print(functools.reduce(operator.add,['Md','Musleh','Uddin']))

# accumulate method
print("The summation of list using accumulate : ",end="")
print(list(itertools.accumulate(lis,lambda x,y : x + y)))