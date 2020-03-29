
"""
Counter:
    - Elements are stored as dictionary keys 
    - Their counts are stored as dictionary values.
"""

from collections import Counter
a = "aaaaabbbbcccccccc"
my_counter = Counter(a)

print(my_counter)
# Counter({'c': 8, 'a': 5, 'b': 4})
print(my_counter.items())
# dict_items([('a', 5), ('b', 4), ('c', 8)])

print(my_counter.keys())
print(my_counter.values())

# Print the most common x element w. freq
print(my_counter.most_common(1))
# Print the most common 1 element w. freq
print(my_counter.most_common(1)[0])
# Print the most common 1 element
print(my_counter.most_common(1)[0][0])

print(list(my_counter.elements()))
# ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
