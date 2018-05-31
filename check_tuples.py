list1 = [1,2]
tuple1 = (1,2,3,4,5,6,4)

print(type(list1))
print(type(tuple1))

#The major difference between tuples and lists is that tuples can not be changed. In technical terms, tuples
#are immutable.

print(tuple1.count(4))
print(3 in tuple1)
print(8 in tuple1)

'''
So what are tuples good for?
• Tuples are faster than lists. If you’re defining a constant set of values and all you’re ever going to do with it
is iterate through it, use a tuple instead of a list.
• It makes your code safer if you “write-protect” data that doesn’t need to be changed. Using a tuple instead
of a list is like having an implied assert statement that shows this data is constant, and that special thought
(and a specific function) is required to override that.
• Some tuples can be used as dictionary keys, as you’ll see later in this chapter. (Lists can never be used as
dictionary keys.)
* To create a tuple of one item, you need a comma after the value. Without the comma, Python just assumes
you have an extra pair of parentheses, which is harmless, but it doesn’t create a tuple.

'''

v = ('a', 2, True)
(x,y,z) = v
print(x,y,z)
print(x)

d = range(11,14)
print(d)
(f,g,h) = d
print(f,g,h)
print(f)
