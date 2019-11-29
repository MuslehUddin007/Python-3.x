'''
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(),float(input())])

'''
n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]
print(marksheet)

second_lowest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_lowest]))

'''
# 1 item will be selected
sl = sorted(marksheet,key=lambda x:x[1])[1]
print(sl[0])
'''