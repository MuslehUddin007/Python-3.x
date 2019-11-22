"""
Return True or False
str.endswith(suffix,start,end)
suffix - string or tuple of suffixes to be checked.
start - index
end - index
"""
#String
text = "Python is easy to learn."
result = text.endswith("to learn") #False
print(result)
result = text.endswith("to learn.") #True
print(result)

result = text.endswith("is",0,14)#False
print(result)
result = text.endswith("easy",0,14)#True
print(result)

#Tuple
result = text.endswith(('python','easy','learn.')) # True
print(result)

result = text.endswith(('is','easy'),0,14) # True
print(result)

