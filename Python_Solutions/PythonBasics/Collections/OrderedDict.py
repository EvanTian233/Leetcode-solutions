"""
Ordered dictionaries 
    - are just like regular dictionaries 
    - but have some extra capabilities relating to ordering operations. 

No longer needed for Python 3.7+
"""

from collections import OrderedDict

# One way
ordered_dic = OrderedDict()
ordered_dic['a'] = 1
ordered_dic['b'] = 2
ordered_dic['c'] = 3
ordered_dic['d'] = 4


# Another way
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
print(''.join(d.keys()))
# 'acdeb'
d.move_to_end('b', last=False)
print(''.join(d.keys()))
# 'bacde'