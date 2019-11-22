def addition(n):
    return n + n

number1 = [1,2,3,4]
result = map(addition,number1)
print(list(result))

result = map(lambda x: x + x, number1)
print(list(result))

number2 = [4,5,6]
result = map(lambda x,y : x + y, number1,number2)
print(list(result))

l = ['sat','bat','cat','mat']
test = list(map(list,l))
print(test)

