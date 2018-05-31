set1= { 1,2,1,3}
print(set1)

list = [ 11, 12, 11, 16]
set2 = set(list)
print(set2)

#Due to historical quirks carried over from Python 2, you can not create an empty set with two curly
#brackets. This actually creates an empty dictionary, not an empty set.
empty_dict = {}
print(type(empty_dict))
empty_set=set()
print(type(empty_set))
print(len(empty_set))

empty_set.add(2)
print(empty_set)

empty_set.update({1,2,3,4})
print(empty_set)

empty_set.update([1,2,3,4,5])
print(empty_set)

'''
1. The discard() method takes a single value as an argument and removes that value from the set.
2. If you call the discard() method with a value that doesn’t exist in the set, it does nothing. No error; it’s
just a no-op.
3. The remove() method also takes a single value as an argument, and it also removes that value from the set.
4. Here’s the difference: if the value doesn’t exist in the set, the remove() method raises a KeyError exception.
'''

empty_set.discard(1)
print(empty_set)
empty_set.discard(1)
print(empty_set)
empty_set.remove(2)
print(empty_set)
try:
    empty_set.remove(2)
except KeyError:
    print("No such element")
print(empty_set)

print(empty_set.pop()) # since sets are unordered pop return random element

'''
clear
union
difference
intersection
symmetric_difference
issuperset
issubset
in

'''