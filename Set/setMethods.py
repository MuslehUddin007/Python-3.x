# union() 
set1 = {2,4,5,6}
set2 = {4,6,7,8}
set3 = {7,8,9,10}

#union two set
print("set1 U set2 : ",set1.union(set2))

#union three sets
print("set1 U set2 U set3 : ",set1.union(set2,set3))

# difference
print("Difference : ",set1.difference(set2))
print("Difference : ",set2-set3)

# difference_update
set1.difference_update(set2)
print('Set1 : ',set1)

# discard don't raise any exception if there isn't that elements
# remove raise exception if there isn't that elements
set2.discard(8)

#intersection
print('Intersection : ',set2.intersection(set3))
# intersection_update method

# Two ses are said to be disjoint when their intersection is null.
print('set1 and set2 are disjoint? ',set1.isdisjoint(set2))

# issubset return True if subset else False
# issuperset return True if superset else False

# symmetric_difference() 
print("Symmetric Differcnce: ",set2.symmetric_difference(set3)) # print(set2 ^ set3)
# symmetric_difference_update()
