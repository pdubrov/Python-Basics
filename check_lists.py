list1 = [1, "w", 2.0, -13, "ttt"]
print(list1)
print(list1[4])
print(list1[-2])
print(list1[2:4])

list1 = list1 + [22, 33] #creates new list, not memory efficient
print(list1)

list1.append(44)
print(list1)

list1.extend([66, 77])
print(list1)

list1.insert(0, 88)
print(list1)

list1.append(44)

print(list1.count(44))

print(-13 in list1)

print(list1.index(88))

del list1[3]
print(list1)

list1.remove(66)
print(list1)

print(list1.pop()) #When called without arguments, the pop() list method removes the last item in the list and returns the value
                   #it removed.
print(list1)

list1 = list(open('C:\Dev\Py\examples/barca.txt', encoding='utf-8'))
lines = sorted(list1)
print(lines)

# sorted accepts also key function which is used for sorting. Here it is len, will sort by length
lines = sorted(list1, key=len)
print(lines)