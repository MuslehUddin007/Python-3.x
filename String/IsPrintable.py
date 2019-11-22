"""
Letter and symbols
digits
punctuation
whitespace
New line not printable
"""

s = "Space is a printable"
print("{} : {}".format(s,s.isprintable()))

s = "\nNew Line is printable"
print("{} : {}".format(s,s.isprintable()))



