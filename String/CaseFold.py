"""The casefold() method is an aggressive lower() method which convert strings to casefolded strings for caseless matching.
"""

firstStr = "Md Musleh Uddin"
secondStr = "md Musleh uddin"

if firstStr.casefold() == secondStr.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal')


