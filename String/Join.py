"""
The join() is a string method which returns a string concatenated with the elements of an iterable.
Iterable (list,string and tuple)
str.join(iterable)
"""

numList = ['1','2','3','4']
seperate = ', '
print(seperate.join(numList))

s1 = 'abc'
s2 = '123'

""" Each character of s2 is concatenated to the front of s1 """
print('s1.join(s2) : ',s1.join(s2))

test = {'Python','Java','C++','C','SQL'}
s = '->->'
print(s.join(test))

test = {'mat': 1, 'that': 2}
s = '->'
print(s.join(test))

#give error if key not string raises TypeError exception.

