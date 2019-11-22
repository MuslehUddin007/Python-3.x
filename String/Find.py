"""
Find() method returns the index of first occurrence of hte substring(if found). If not found return -1.

str.find(sub,start,end)
"""

quote = "Let it be, let it be, let it be"
result = quote.find('let it')
print("Substring 'let it': ",result)

if(quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")

print("With start and end : ",quote.find("let it",10,20))

""" The rfind() method returns the highest index of the substring if found. """
result = quote.rfind('let it')
print("Substring 'let it': ",result)

