import numpy as np

arr = np.array([[1,2,3],
                [4,2,5]])
print("Array is of type : ",type(arr))
print("No. of dimensions : ",arr.ndim)
print("Shape of array : ",arr.shape)
print("Size of array : ",arr.size)
print("Array stores elements of type : ",arr.dtype)

a = np.array([[1,2,4],[5,8,7]],dtype = 'float')
print("Array created using passed list : ",a)

c = np.zeros((3,4))
print("An array initialized with all zeros: ",c)

d = np.full((3,3),6,dtype='complex')
print("An array initialized with all 6s."
      "Array type is complex : ",d)

print("A random array : ",np.random.random((2,2)))
arr = np.array([[1,2,3],[4,5,6]])
flarr = arr.flatten()
print("Fattend array : ",flarr)