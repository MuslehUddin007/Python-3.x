""" map(function, iterable, ...) """
def calSquare(n):
    return n*n

numbers = (1,2,3,4,5)
result = map(calSquare,numbers)
print(set(result))

result = map(lambda x: x*x, numbers)
print(set(result))

#multiple iteration
num1 = [4,5,6]
num2 = [5,6,7]

result = map(lambda n1, n2: n1+n2, num1,num2)
print(list(result))