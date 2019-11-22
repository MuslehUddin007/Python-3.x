""" 
The strip() method returns a copy of the string with both leading and trailing characters removed.
"""

str = "xoxo love xoxo"
print(str.strip())
print(str.strip(' xoxoe'))

""" inside strip string start with space then it act like char else act like string """
rstr = "This is right strip   "
lstr = "   This is left strip"
print(rstr.rstrip())
print(lstr.lstrip())

