"""
\   Used to drop the special meaning of character
    following it (discussed below)
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One ore more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs
"""

import re

p = re.compile('[a-e]')
print(p.findall("Aye, said Mr. Gibenson Stark"))


"""
\d   Matches any decimal digit, this is equivalent
     to the set class [0-9].
\D   Matches any non-digit character.
\s   Matches any whitespace character.
\S   Matches any non-whitespace character
\w   Matches any alphanumeric character, this is
     equivalent to the class [a-zA-Z0-9_].
\W   Matches any non-alphanumeric character. 
"""
p = re.compile('\w')
print(p.findall("He said * in some_long."))

p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

p = re.compile('\W')
print(p.findall("he said *** in some_language."))

# '*' replaces the no. of occurrence of a character.
p = re.compile('ab*')
print(p.findall("ababbaabbb"))

# re.split(pattern,string,maxsplit=0,flags=0)
print(re.split('\d+','On 12th Jan 2016, at 11.02 AM',1))

print(re.split('[a-f]+','Aye, Boy oh boy, come here',4,flags=re.IGNORECASE))

# re.sub(patern,repl,string,count=0,flags=0)
print(re.sub('ub','~*','Subject has Uber booked already',count=1,flags=re.IGNORECASE))

print(re.subn('ub','~*','Subject has Uber booked alreaady',flags=re.IGNORECASE))

# re.escape(string)
print(re.escape("I Asked what is this [1-9], he said \t ^WOW"))