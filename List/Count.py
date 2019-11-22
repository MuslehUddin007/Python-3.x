list1 = [1,1,1,2,3,3,2,1]
print(list1.count(1))

list2 = ['cat','bat','sat','cat','Cat','mat']
print(list2.count('cat'))

print([[l,list2.count(l)] for l in set(list2)])

# dictionary
print(dict((l,list2.count(l)) for l in set(list2)))