class PapayaWhip:
    pass
# pass - no-op, equivalent to {} in java

'''
The __init__() method is called immediately after an instance of the class is created. 
It would be tempting — but technically incorrect — to call this the “constructor” of the class. 
Incorrect, because the object has already been constructed by the time the __init__()
method is called, and you already have a valid reference to the new instance of the class.
'''
class Fib1:
    '''
    1. Each instance of the class inherits the rules_filename attribute with the value defined by the class.
2. Changing the attribute’s value in one instance does not affect other instances…
3. …nor does it change the class attribute. You can access the class attribute (as opposed to an individual
instance’s attribute) by using the special __class__ attribute to access the class itself.
4. If you change the class attribute, all instances that are still inheriting that value (like r1 here) will be affected.
5. Instances that have overridden that attribute (like r2 here) will not be affected.
'''
    name = 'Fibonacci'

    '''iterator that yields numbers in the Fibonacci sequence'''
    def __init__(self, max):
        pass
    '''
    The first argument of every class method, including the __init__() method, is always a reference to the
current instance of the class. By convention, this argument is named self. This argument fills the role of the
reserved word this in C + + or Java, but self is not a reserved word in Python, merely a naming
convention. Nonetheless, please don’t call it anything but self; this is a very strong convention.
In the __init__() method, self refers to the newly created object; in other class methods, it refers to the
instance whose method was called. Although you need to specify self explicitly when defining the method,
you do not specify it when calling the method; Python will add it for you automatically.
    '''
    def some_method(self):
        pass

import fibonacci
'''
To instantiate a class, simply call the class as if it were a
function, passing the arguments that the __init__() method requires. The return value will be the newly
created object.
'''
fib = fibonacci.Fib(200)
print(fib.__doc__)
print(fib.__class__)

'''
The for loop calls Fib(1000), as shown. This returns an instance of the Fib class. Call this fib_inst.
• Secretly, and quite cleverly, the for loop calls iter(fib_inst), which returns an iterator object. Call this
fib_iter. In this case, fib_iter == fib_inst, because the __iter__() method returns self, but the for loop
doesn’t know (or care) about that.
• To “loop through” the iterator, the for loop calls next(fib_iter), which calls the __next__() method on
the fib_iter object, which does the next-Fibonacci-number calculations and returns a value. The for loop
takes this value and assigns it to n, then executes the body of the for loop for that value of n.
• How does the for loop know when to stop? I’m glad you asked! When next(fib_iter) raises a
StopIteration exception, the for loop will swallow the exception and gracefully exit. (Any other exception
will pass through and be raised as usual.) And where have you seen a StopIteration exception? In the
__next__() method, of course!
'''
for n in fibonacci.Fib(1000):
    print(n, end=' ')

a = Fib1(30)
b = Fib1(20)

b.name = 'uhu'

print("{0} / {1}".format(a.name, b.name))
print("{0} / {1}".format(a.__class__.name, b.__class__.name))