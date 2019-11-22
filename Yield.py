"""
We yield resumed, the function continues execution immediately after the last yield run.
"""


# Generators function
def fun():
    yield 1
    yield 2
    yield 3

for value in fun():
    print(value)

# fibonacci number
def fib(limit):
    a, b = 0, 1
    while a<limit:
        yield a
        a, b = b, a + b

print("Using for in loop")
for i in fib(10):
    print(i)


# sequence of number
def nextSquare():
    i = 1
    while True:
        yield i*i
        i += 1 # next execution resumes from this point

for num in nextSquare():
    if num > 100:
        break
    print(num)


