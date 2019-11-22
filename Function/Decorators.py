def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print('This is after function execution')
    return inner1

def function_to_be_used():
    print('This is inside the function !!')

function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()

# execution of time
import time
import math

def calculate_time(func):
    def inner1(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end = time.time()
        print('Totol time taken in : ',func.__name__,end - begin)
    return inner1

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(10)

# another example
def hello_decorator(func):
    def inner1(*args,**kwargs):
        print('Before Execution')
        returned_value = func(*args,**kwargs)
        print('After Execution')
        return returned_value
    return inner1

@hello_decorator
def sum_two_numbers(a,b):
    print('Inside the function')
    return a+b
a, b = 1, 2
print("Sum = ",sum_two_numbers(a,b))