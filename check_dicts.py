dict1 = { "a":1, "b":2, 'c':3}
print(dict1)
print(dict1["a"])
dict1['i']=90
dict1['c']=30
print(dict1)

print(type(None))
print(None==False)

characters = ('S', 'M', 'E', 'D', 'O', 'N', 'R', 'Y')
guess = ('1', '2', '0', '3', '4', '5', '6', '7')
print(tuple(zip(characters, guess)))
print(dict(zip(characters, guess)))