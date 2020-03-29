"""
Chain Map:
    - dict-like class for creating a single view of multiple mappings
    - A ChainMap groups multiple dicts or other mappings together 
    - to create a single, updateable view. If no maps are specified, 
    - a single empty dictionary is provided so that a new chain always has at least one mapping.
"""

from collections import ChainMap
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(list(ChainMap(adjustments, baseline)))
# ['music', 'art', 'opera']