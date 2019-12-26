"""List = []
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'insert':
        List.insert(int(command[1]),int(command[2]))
    elif command[0] == 'remove':
        List.remove(int(command[1]))
    elif command[0] == 'append':
        List.append(int(command[1]))
    elif command[0] == 'sort':
        List.sort()
    elif command[0] == 'pop':
        if len(List) == 0:
            pass
        else:
            List.pop()
    elif command[0] == 'reverse':
        List = List[::-1]
    else:
        print(List)
"""
n = int(input())
arr = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        eval('arr.{0}{1}'.format(cmd,tuple(map(int,args))))
    else:
        print(arr)