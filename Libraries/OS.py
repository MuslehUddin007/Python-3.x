import os

print(os.name)
print(os.getcwd())

try:
    filename = 'GFG.txt'
    f = open(filename,'rU')
    text = f.read()
    f.close()
except IOError:
    print("Problem reading : "+filename)