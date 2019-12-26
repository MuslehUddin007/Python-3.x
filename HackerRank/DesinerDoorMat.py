size = input().split()
n = int(size[0])
m = int(size[2])

pattern = [('.|.'*(2*i + 1)).center(m,'-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m,'-')] + pattern[::-1]))