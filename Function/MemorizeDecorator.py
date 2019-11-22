def memorize_factorial(f):
    memory = {}
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]
    return inner
@memorize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)

print(facto(10))