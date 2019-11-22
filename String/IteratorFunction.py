import itertools
import operator

li1 = [1,4,5,7]
li2 = [1,6,5,9]
li3 = [8,10,5,4]
li4 = [li1,li2,li3]

#Accmulate
print('The sum after each iteration is : ',end="")
print(list(itertools.accumulate(li1)))

#Accmulate with operator
print('The product after each iteration is : ',end="")
print(list(itertools.accumulate(li1,operator.mul)))

#Chain
print("All values in mentioned chain are : ",end="")
print(list(itertools.chain(li1,li2,li3)))

#Chain from_iterable
print("All values in mentioned chain are : ",end="")
print(list(itertools.chain.from_iterable(li4)))

#compress
print("The compressed values in string are : ",end="")
print(list(itertools.compress('MDMUSLEHUDDINKHANAKIL',[1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0])))

#dropwhile
print('The value after condition returns false : ',end="")
print(list(itertools.dropwhile(lambda x: x%2 == 0, li1)))

#filterfalse
print('The value that return false to function are : ',end="")
print(list(itertools.filterfalse(lambda x: x%2 == 0,li1)))

# islice(list,start,end,difference)
print('The sliced list values are : ',end="")
print(list(itertools.islice(li1,1,3,2)))

#starmap
li5 = [(1,10,5),(8,4,1),(5,4,9),(11,10,1)]
print('The values acc. to function are : ',end="")
print(list(itertools.starmap(min,li5)))

# takewhile is oppisite of dropwhile
#zip_longer
print('The combined values of iteratbles is : ')
print(*(itertools.zip_longest('Mmseudi','dulhdn',fillvalue='_')))

#product
print('The cartesian product of the containers is : ')
print(list(itertools.product('AB','12')))

# permutations
print('All the permutations of the given container is : ')
print(list(itertools.permutations('MUS',2)))
#combinations like permutations
#combinations_with_replacement

# repeat(12,4) 
# output [12,12,12,12]