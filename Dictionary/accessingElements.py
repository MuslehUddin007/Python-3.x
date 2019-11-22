#dictionary
test_dict = {1:'Md',2:'Musleh',3:'Uddin',4:'Khan',5:'Akil'}

# loop
print("Dict key-value using loop : ")
for i in test_dict:
    print(i,test_dict[i])

#using list comprehension
print("dict key-value using list comprehension : ")
print([(k,test_dict[k]) for k in test_dict])

# dict.item()
print("Dict key-value using items : ")
for key,value in test_dict.items():
    print(key, value)

# enumerate
print("Dict key-value using enumerate : ")
for i in enumerate(test_dict.items()):
    print(i)

