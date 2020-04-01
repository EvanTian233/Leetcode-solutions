"""
Defalut Dict:
    - dict subclass that calls a factory function to supply missing values
    - Similar to usual container
    - Have defalt value if key is not been set yet
"""

from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)


"""
Using list as the default_factory, 
it is easy to group a sequence of key-value pairs into a dictionary of lists
"""
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(sorted(d.items()))
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


"""
Setting the default_factory to int 
makes the defaultdict useful for counting 
(like a bag or multiset in other languages):
"""

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

print(sorted(d.items()))
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]