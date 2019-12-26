s = input()
vawels = 'AEIOU'

kevsc = 0
stusc = 0

for i in range(len(s)):
    if s[i] in vawels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)
if kevsc>stusc:
    print("Kevin %d"%(kevsc))
elif kevsc<stusc:
    print("Stuart %d"%(stusc))
else:
    print("Draw")