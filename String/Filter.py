alp = ['a','b','c','d','e','f','g','h','i']

def filterVowels(alp):
    vowels = ['a','e','i','o','u']
    if (alp in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels,alp)
print("The filtered Vowels are: ")
for vowel in filteredVowels:
    print(vowel)

"""If item is true put it on list else remove """
