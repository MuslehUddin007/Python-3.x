"""
all tab characters \t replaced with whitespace.
default tabsize is 8
"""

str = "Md\tMusleh\tUddin\t"
result = str.expandtabs()
print(result)

result = str.expandtabs(4)
print(result)

#tabsize 4. The tab stops are 4,8,12 and so on.
