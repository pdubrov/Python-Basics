import os, glob

a_list = [1, 9, 8, 4]

b_list = [elem * 2 for elem in a_list]

print(b_list)

print([os.path.realpath(f) for f in glob.glob('*.py') if os.stat(f).st_size > 600])

# list comprehension, results in a list of tuples
metadata = [(f, os.stat(f).st_mtime) for f in glob.glob('*.py')]
print(metadata)

# dictionary comprehension
metadata_dict = {f: os.stat(f) for f in glob.glob('*.py')}
print(metadata_dict)

print(metadata_dict["check_dicts.py"])

meta_dict1 = {os.path.splitext(f)[0]: meta.st_size \
              for f, meta in metadata_dict.items() if meta.st_size > 600}

print(meta_dict1)

#swap keys and values of a dictionary
swapped_dict = {value:key for key, value in meta_dict1.items()}
print(swapped_dict)

#set comprehensions
a_set = set(range(10))
print(a_set)
a_set={x ** 2 for x in a_set}
print(a_set)
a_set={x for x in a_set if x % 2 == 0}
print(a_set)
b_set={2**x for x in range(10)} 
print(b_set)

# This is generator function and NOT tuple comprehension
unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
gen = (ord(c) for c in unique_characters)