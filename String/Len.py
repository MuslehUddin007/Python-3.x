testDict = {1:'one',2:'two'}
print(testDict, 'length is', len(testDict))

class Session:
    def __init__(self,number = 0):
        self.number = number

    def __len__(self):
        return self.number

s1 = Session()
print(len(s1))

s2 = Session(6)
print(len(s2))