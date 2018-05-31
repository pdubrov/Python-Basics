import itertools

# Combinatorics - set of all permutations
print(set(itertools.permutations([1, 2, 3 ], 2)))
print(tuple(itertools.permutations("ABCD", 2)))

'''
1. The itertools.product() function returns an iterator containing the Cartesian product of two sequences.
2. The itertools.combinations() function returns an iterator containing all the possible combinations of the
given sequence of the given length. This is like the itertools.permutations() function, except combinations
don’t include items that are duplicates of other items in a different order.
'''

print(tuple(itertools.product("ABC", {2,1})))
print(tuple(itertools.combinations("ABCD", 2)))

#groupby
names = ["Alfred", "Nadya", "Chichako", "Gavrila", "Pedro", "Anton"]
names = sorted(names, key=len) #The itertools.groupby() function only works if the input sequence is already sorted
                                #by the grouping function.
groups = itertools.groupby(names, len) # returns iterator
print(groups)

print(list(groups)) # list exhausts iterator

# creating new one
groups = itertools.groupby(names, len)
for name_length, name_iter in groups:
   print('Names with {0:d} letters:'.format(name_length))
   for name in name_iter:
       print(name)


# chain/zip
print(list(range(0, 3)))

'''
The itertools.chain() function takes two iterators and returns an iterator that contains all the items from
the first iterator, followed by all the items from the second iterator. (Actually, it can take any number of
iterators, and it chains them all in the order they were passed to the function.)
'''
print(list(itertools.chain(range(0, 3), range(10, 13))))

'''
The zip() function takes any number of sequences and returns an iterator which returns tuples 
of the first items of each sequence, then the second items of each, then the third, and so on.'''
print(list(zip(range(0, 3), range(10, 13))))
#The zip() function stops at the end of the shortest sequence.
print(list(zip(range(0, 3), range(10, 14))))
#the itertools.zip_longest() function stops at the end of the longest sequence, inserting
#None values for items past the end of the shorter sequences.
print(list(itertools.zip_longest(range(0, 3), range(10, 14))))


