def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('incrementing x')
        x = x + 1

'''The presence of the yield keyword in make_counter means that this is not a normal function. It is a special
kind of function which generates values one at a time. You can think of it as a resumable function. Calling it
will return a generator that can be used to generate successive values of x.'''

'''2. To create an instance of the make_counter generator, just call it like any other function. Note that this does
not actually execute the function code.'''
counter = make_counter(2)
print(counter)

'''The next() function takes a generator object and returns its next value. The first time you call next() with
the counter generator, it executes the code in make_counter() up to the first yield statement, then returns
the value that was yielded. In this case, that will be 2, because you originally created the generator by calling
make_counter(2).
5. Repeatedly calling next() with the same generator object resumes exactly where it left off and continues
until it hits the next yield statement. All variables, local state, &c. are saved on yield and restored on
next().'''

print(next(counter))
print(next(counter))
print(next(counter))


def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

'''This is a useful idiom: pass a generator to the list() function, and it will iterate through the entire
generator (just like the for loop in the previous example) and return a list of all the values.'''
print(list(fib(200)))

'''You can use a generator like fib() in a for loop directly. The for loop will automatically call the next()
function to get values from the fib() generator and assign them to the for loop index variable (n).'''
for n in fib(1000):
    print(n, end=' ')

    '''What have you gained over stage 4? Startup time. In stage 4, when you imported the plural4 module, it
read the entire patterns file and built a list of all the possible rules, before you could even think about calling
the plural() function. With generators, you can do everything lazily: you read the first rule and create
functions and try them, and if that works you don’t ever read the rest of the file or create any other
functions.
What have you lost? Performance! Every time you call the plural() function, the rules() generator starts
over from the beginning — which means re-opening the patterns file and reading from the beginning, one line
at a time.'''


#Generator functions
# This is generator function and NOT tuple comprehension
unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
gen = (ord(c) for c in unique_characters)
print(gen)
print(tuple(gen))

'''
A generator expression is like an anonymous function that yields values. The expression itself looks like a list
comprehension, but it’s wrapped in parentheses instead of square brackets.
2. The generator expression returns… an iterator.
3. Calling next(gen) returns the next value from the iterator.
4. If you like, you can iterate through all the possible values and return a tuple, list, or set, by passing the
generator expression to tuple(), list(), or set(). In these cases, you don’t need an extra set of
parentheses — just pass the “bare” expression ord(c) for c in unique_characters to the tuple() function,
and Python figures out that it’s a generator expression.

!!!Using a generator expression instead of a list comprehension can save both C P U and
R A M . If you’re building an list just to throw it away (e.g. passing it to tuple() or
set()), use a generator expression instead!
'''