class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''

    '''All three of these class methods, __init__, _iter__, and __next__, begin and end
with a pair of underscore (_) characters. Why is that? There’s nothing magical about it, but it
usually indicates that these are “special methods.” The only thing “special” about special
methods is that they aren’t called directly; Python calls them when you use some other
syntax on the class or an instance of the class.'''
    def __init__(self, max):
        self.max = max  #instance variable

    '''
The __iter__() method is called whenever someone calls iter(fib). (As you’ll see in a minute, a for loop
will call this automatically, but you can also call it yourself manually.) Called once
'''
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self


    '''The __next__() method is called whenever someone calls next() on an iterator of an instance of a class.
    When the __next__() method raises a StopIteration exception, this signals to the caller that the iteration is
exhausted. Unlike most exceptions, this is not an error; it’s a normal condition that just means that the
iterator has no more values to generate. If the caller is a for loop, it will notice this StopIteration
exception and gracefully exit the loop. (In other words, it will swallow the exception.) This little bit of magic
is actually the key to using iterators in for loops.
'''
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

'''
iter(f) calls f.__iter__
next(f) calls f.__next__
'''