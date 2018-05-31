import re

'''^ matches the beginning of a string.
◦ $ matches the end of a string.
◦ \b matches a word boundary.
◦ \d matches any numeric digit.
148
◦ \D matches any non-numeric character.
◦ x? matches an optional x character (in other words, it matches an x zero or one times).
◦ x* matches x zero or more times.
◦ x+ matches x one or more times.
◦ x{n,m} matches an x character at least n times, but not more than m times.
◦ (a|b|c) matches either a or b or c.
◦ (x) in general is a remembered group. You can get the value of what matched by using the groups() method
of the object returned by re.search.
* The square brackets mean “match exactly one of these characters.” So [sxz] means “s, or x, or z”, but only one of them.
* The ^ as the first character inside the square brackets means
something special: negation. [^abc] means “any single character except a, b, or c”.
* (.*?) - shortest possible series of any character

'''

# re.sub() function performs regular expression-based string substitutions.
s = '100 NORTH BROAD ROAD'
print("{0} -> {1}".format(s, re.sub("ROAD$", "RD.", s)))

#To work around the backslash plague, you can use what is called a raw string, by prefixing the string with the
#letter r.

print("gh\tyahii")
print(r"gh\tyahii")

#\b, which means “a word boundary must occur right here.

s='100 BROAD ROAD APT. 3'
print(re.sub(r'\bROAD\b', 'RD.', s))

# ^ matches what follows only at the beginning of the string.
# And $ matches the end of the string

#M? optionally matches a single M character.
pattern = '^M?M?M?$'
#If a match is found, search() returns an object which has various methods to describe the match;
# if no match is found, search() returns None, the Python null value.
match = re.search(pattern, "MMM")
print(match.group(0))

#pattern equivalent to pattern below
pattern1 = '^M{0,3}$'

pattern2 = '^M?M?M?(CM|CD|D?C?C?C?)$'

'''A verbose regular expression
is different from a compact regular expression in two ways:
◦ Whitespace is ignored. Spaces, tabs, and carriage returns are not matched as spaces, tabs, and carriage
returns. They’re not matched at all. (If you want to match a space in a verbose regular expression, you’ll
need to escape it by putting a backslash in front of it.)
◦ Comments are ignored. A comment in a verbose regular expression is just like a comment in Python code:
it starts with a # character and goes until the end of the line. In this case it’s a comment within a multi-line
string instead of within your source code, but it works the same way.'''

pattern = '''
^ # beginning of string
M{0,3} # thousands - 0 to 3 Ms
(CM|CD|D?C{0,3}) # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
# or 500-800 (D, followed by 0 to 3 Cs)
(XC|XL|L?X{0,3}) # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
# or 50-80 (L, followed by 0 to 3 Xs)
(IX|IV|V?I{0,3}) # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
# or 5-8 (V, followed by 0 to 3 Is)
$ # end of string
'''

match = re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE);

print(match.group(1))

# \d matches any numeric digit (0–9). \D matches anything but digits.
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(phonePattern.search('800-555-1212').groups())


print(re.findall("[0-9]+", "231 huh 7 iojo8 jj9"))
#it doesn’t return overlapping matches