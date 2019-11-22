"""
Partition() split  at the first occurrence.
rpartition() split at last occurrence.
"""
str = "Python is fun"
print(str.partition("is"))

str = "Python is fun, isn't it"
print(str.partition("is"))

print(str.rpartition("is"))


