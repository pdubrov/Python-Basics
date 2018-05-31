print(eval('9567 + 1085 == 10652'))

'''
The eval() function isn’t limited to boolean expressions. It can handle any Python
expression and returns any datatype.
'''

import subprocess
print(eval("subprocess.getoutput('dir')"))
print(eval("__import__('subprocess').getoutput('dir')"))

# eval is UNSAFE. Never eval commands from untrusted sources

x=5
try:
    print(eval("x * 5", {}, {}))
except NameError:
    print("Error catched",eval("x * 5", {"x": x}, {}))  # works
'''
The second and third parameters passed to the eval() function act as the global and local namespaces for
evaluating the expression. In this case, they are both empty, which means that when the string "x * 5" is
evaluated, there is no reference to x in either the global or local namespace, so eval() throws an exception.
You can selectively include specific values in the global namespace by listing them individually. Then
those — and only those — variables will be available during evaluation.

'''


import math
try:
    print(eval("math.sqrt(x)", {"x": x}, {}))
except NameError:
    print("Error catched", eval("math.sqrt(x)", {"x": x}, { "math":math }))  # works

'''
all of Python’s built-in functions are still available during evaluation
__import__() function is also a built-in, so need to be careful
'''
print(eval("pow(5,2)", {}, {}))


#Is there any way to use eval() safely?
'''
To evaluate untrusted expressions safely, you need to define a global namespace dictionary that maps
"__builtins__" to None, the Python null value. Internally, the “built-in” functions are contained within a
pseudo-module called "__builtins__". This pseudo-module (i.e. the set of built-in functions) is made available
to evaluated expressions unless you explicitly override it.
'''
try:
    eval("__import__('math').sqrt(5)", {"__builtins__":None}, {})
except TypeError:
    print("Can't use built-in functios when __builtin__ is overridden")

'''    So eval() is safe now? Well, yes and no.
    1. Even without access to __builtins__, you can still launch a denial-of-service attack.
    eval("2 ** 2147483647", {"__builtins__":None}, {})
'''
