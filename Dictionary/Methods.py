# popitem() remove dublicate key value
test_dict = {'Musleh':1,'Uddin':2,'Musleh':3}
print("Before Deletion: "+str(test_dict))
res = test_dict.popitem()
print("After Deletion: "+str(res))

# get 
print(test_dict.get('Musleh'))
print(test_dict.get('Uddin','Not Found !'))

# values()
print(test_dict.values())

salary = {'raj':50000,'khan':60000,'musleh':1000000}
list1 = salary.values()
print('Total Value : ',sum(list1))

# default value
Forth_value = salary.setdefault('musleh')
print(Forth_value)

# keys
print(salary.keys())

# accessing keys using loop
j=0
for i in salary:
    if(j==1):
        print('2nd key using loop : ' + i)
    j = j + 1

# accessing key using keys()
print('2nd key using keys() : ' + list(salary.keys())[1])

#items() method show dictionary item
# has_key - remove in python 3.x
#print('Check Musleh present : ',salary.has_key('musleh'))

# fromkeys
seq = {'a','b','c','d','e'}
res_dict = dict.fromkeys(seq)
print(res_dict)
res_dict2 = dict.fromkeys(seq,2)
print(res_dict2)

lis1 = [2,3]
res_dict3 = {key : list(lis1) for key in seq}
print(res_dict3)