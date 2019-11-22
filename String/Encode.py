"""
#str.encode(encoding='UTF-8',errors='strict')
#encoding version = utf-8,ascii
#*encoding - the encoding type a string has to be encoded to
#*errors - response when encoding fails. There are six types of error response
#1. strict = default response which raises a UnicodeDecodeError exception on failure
#2. ignore = ignores the unencodable unicode from the result
#3. replace = replaces the unencodable unicode to a question mark ?
#4. xmlcharrefreplace = insert XML character reference instead of unencodable unicode
#5. backslashreplace = insert a \uNNNN espace sequence instead of unencodable unicode
#6. nameereplace = insert a \N excape squence instead of unencodable unicode
"""

str = "I wanna say pyth\xc3\xb6n!"
str_utf = str.encode()
print("UTF-8 : ",str_utf)

str_asc = str.encode("ascii","replace")
print("ASCII : ",str_asc)
