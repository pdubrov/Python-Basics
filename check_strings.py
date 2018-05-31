import sys,first,functions
s = '深入 Python'

print(len(s))

name = "Pav"
surname = "Dubrouski"

print("{0} with surname {1}".format(name, surname))

'''
format specifers can
access items and properties of data structures using (almost)
Python syntax. This is called compound field names. The
following compound field names “just work”:
• Passing a list, and accessing an item of the list by index
(as in the previous example)
• Passing a dictionary, and accessing a value of the
dictionary by key
• Passing a module, and accessing its variables and
functions by name
• Passing a class instance, and accessing its properties and
methods by name
• Any combination of the above
'''

print(sys.modules['functions'].some_func("iii"))

#print("{0.modules[functions].some_func(Pavel)} hello".format(sys))

print('{0:.5f} {1}'.format(698.24234324, 'GB'))

s = '''The EOS.IO Testnet has arrived. 
       Scalable decentralized applications 
       can now be built and 
       tested in a public environment.'''

list = s.splitlines()
print(list)

print(s.lower())

query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list = query.split('&')
a_list_of_lists = [v.split('=', 1) for v in a_list]
print(a_list_of_lists)
a_dict = dict(a_list_of_lists)
print(a_dict)
print(s[3:18]) #slicing

words = [ "my", "name", "is", "Pavel"]
print(''.join(words))
print(set(''.join(words)))

translation_table = {ord('A'): ord('O')}
print('MARK'.translate(translation_table))

import string
trans_dict = str.maketrans( string.punctuation, " "*len(string.punctuation))
print("Price! is the, same".translate(trans_dict))