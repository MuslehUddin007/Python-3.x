#using max(arg1,arg2,*args)
print('Maximun is : ',max(1,2,3,5,4))

#using max(iterable)
num = [1,3,2,8,5,10,6]
print('Maximum is : ',max(num))

def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

#using max(arg1,arg2,*args,key)
print('Maximum is : ',max(100,321,267,59,40, key=sumDigit))

#using max(iterator, key)
num = [15,300,2700,821,52,10,6]
print('Maximum is : ',max(num,key=sumDigit))

num = [15,300,2700,821]
num1 = [12,2]
num2 = [34,567,78]

#using max(iterable, *iterables, key)
print('Maximum is : ',max(num, num1, num2, key=len))
print('Minimum is : ',min(num, num1, num2, key=len))