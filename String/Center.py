"""
The center() method returns a string which is padded with the specified character. string.center(width,"fillchar")
width - length of the string with padded characters
fillchar(optional) - padding character
"""

str = "Md Musleh Uddin Khan Akil"
str_cen = str.center(40)

print("Centered String: ",str_cen)
str_fill = str.center(40,'*')
print("Centered String with fillchar: ",str_fill)
print("Length: ",len(str_fill))

