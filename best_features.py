# 1 Multiple comparisons
n = 5
print(1 < n < 4000)
print(6 < n < 8)

# 2 Copy list
a = [1, 4, 5]
b = a[:]

print(a == b)
print(a is b)

# 3 StrContains

name = "best Bank of England"
print("Bank" in name)
print("oops" in name)

# 4 unzip using zip(*list)
list1 = (1, 4, 7)
list2 = (2, 5, 8)
list3 = (3, 6, 9)
zipped = list(zip(list1, list2, list3))
print(zipped)
list4, list5, list6 = list(zip(*zipped))
print(list1 == list4)
print(list2 == list5)
print(list3 == list6)

# 5 chunking
iter = iter(range(1, 101))
chunks = list(zip(*[iter] * 10))
print(chunks)
