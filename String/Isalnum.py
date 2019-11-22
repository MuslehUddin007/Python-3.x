""" 
Return True if all characters is alphaumeric else return false.
str.isalnum(); no parameter take
"""

name = "m12m235532m"
print(name.isalnum())

name1 = "ak13r 235kj"
print(name1.isalnum())

if name.isalnum() == True:
    print("Alphanumeric")
else:
    print("Not alphanumeric")


