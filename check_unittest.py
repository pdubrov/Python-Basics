import unittest
import fibonacci

class FibTest(unittest.TestCase):

    '''
Every individual test is its own method, which must take no parameters and return no value. If the method
exits normally without raising an exception, the test is considered passed; if the method raises an exception,
the test is considered failed.
'''
    def test_fibonacci_generator(self):
        ''' Tests fibonacci generator
        '''
        fib = fibonacci.Fib(10)
        self.assertEqual(list(fib), [0, 1, 1, 2, 3, 5, 8])

    def test_fibonacci_generator2(self):
        ''' Tests fibonacci generator2
        '''
        fib = fibonacci.Fib(5)
        list(fib) # exhaust iterator
        self.assertRaises( StopIteration, fib.__next__) # just passing function, do not execute it

if __name__ == '__main__':
    unittest.main(verbosity=2) #unittest.main(), which runs each test case


