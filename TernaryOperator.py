# min value
a, b = 10, 20
min = a if a < b else b
print(a)

# use tuple for selecting an item
print((b,a)[a < b])

# use dictionary 
print({True : a,False : b}[a < b])

#lambda expresion
print((lambda: b, lambda: a)[a < b]())

#nested ternary operator
print("Both a and b are equal" if a==b else "a is greater than b" if a > b else "b is greater than a")

# and or
print(a < b and a or b)
