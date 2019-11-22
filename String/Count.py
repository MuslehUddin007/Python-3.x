"""
Count() method searches the substring in the given string and returns how many times the substring is present in it. str(subStr, start='',end='')
start = starting index within the string where search starts.
end = starting index within the string where search ends.
"""

str = "Python is awesome, isn't it?"
subStr = "is"

count1 = str.count(subStr)
count2 = str.count(subStr,0,18)
print("First count : ",count1)
print("Second count : ",count2)

