numList = [1,2,3]
strList = ['one','two','three']

#zip
result = zip(numList,strList)
result = list(result)
print((result))

#unzip
c , v = zip(*result)
print('c=',c)
print('v=',v)