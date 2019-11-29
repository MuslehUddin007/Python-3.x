"""
h = short in C type
l = long in C type
? = _BOOL
i = int
q = long long int 
f = float
b =  
"""
import struct

var = struct.pack('?hil',True,2,5,445)
print(var)
tup = struct.unpack('?hil',var)
print(tup)