arr = []
inp = '0 5'.split()
a = inp[0:]
b = '6'
eval('arr.{0}{1}'.format('insert',tuple(map(int,a))))
eval('arr.{0}{1}'.format('append',tuple(map(int,b))))
print(arr)
