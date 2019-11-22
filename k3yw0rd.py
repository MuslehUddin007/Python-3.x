import keyword

print("The list of keywords is : ")
print(keyword.kwlist)

print("\nCheck is keyword : ")
s = "try"
if keyword.iskeyword(s):
    print(s + " is a keyword")

else:
    print(s + " is not a keyword")


