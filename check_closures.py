import re
def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

'''This technique of using the values of outside parameters within a dynamic function is called
closures. You’re essentially defining constants within the apply function you’re building: it takes one parameter
(word), but it then acts on that plus two other values (search and replace) which were set when you
defined the apply function.'''

patterns = \
(
('[sxz]$', '$', 'es'),
('[^aeioudgkprt]h$', '$', 'es'),
('(qu|[^aeiou])y$', 'y$', 'ies'),
('$', '$', 's')
)
rules = [ build_match_and_apply_functions(pattern, search, replace)
          for (pattern, search, replace) in patterns ]

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

print(plural("ski"))
print(plural("cheetah"))
print(plural("bed"))