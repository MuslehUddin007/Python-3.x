"""
Identifiers containt = Uppercase, Lowercase, digit and upderscore.
An identifier can't start with a digit.
keywords can't be used as identifier.
Can't containt space.
"""

str = "Python"
print(str.isidentifier())

str = "root33"
if str.isidentifier() == True:
    print("Identifier")
else:
    print("Not Identifier")


