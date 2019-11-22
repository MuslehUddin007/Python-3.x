"""
Index() return index number if found, else raises an exception.
str.index(sub,start,end)
"""
sen = "Python programming is fun,Isn't it is fun"
result = sen.index("is fun")
print("Substring : ",result)

print("Substring : ",sen.index("g is",10,-4))

""" Return the highest index of the substring inside the string """
result = sen.rindex("is fun")
print("RIndex : ",result)
