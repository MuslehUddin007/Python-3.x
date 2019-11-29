import re

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex,"I was born on June 24")

if match != None:
    print("Match at index %s, %s" %(match.start(),match.end()))
    print("Full match : %s" %(match.group(0)))
    print("Month: %s" %(match.group(1)))
    print("Day: %s" %(match.group(2)))
else:
    print("The regex pattern does not match")

text = "MdMuslehUddin"
new_email = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",text,re.I))
print(new_email)