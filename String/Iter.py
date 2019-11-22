vowels = ['a','e','i','o','u']

vowelsIter = iter(vowels)

print(next(vowelsIter)) # 'a'
print(next(vowelsIter)) # 'e'
print(next(vowelsIter)) # 'i'
print(next(vowelsIter)) # 'o'
print(next(vowelsIter)) # 'u'

class PrintNumber:
    def __init__(self,max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

printNum = PrintNumber(3)
PrintNumIter = iter(printNum)

print(next(PrintNumIter)) # '1'
print(next(PrintNumIter)) # '2'
print(next(PrintNumIter)) # '3'
print(next(PrintNumIter)) # StopIteration