"""
Reduce:
    - Applies same operation to items of a sequence
    - User result of operation as first param of next operation
    - Return an item, not a list
"""

from functools import reduce

def mult(lst1):
    prod = lst1[0]
    for i in range(1, len(lst1)):
        prod *= lst1[i]
    return prod

print(mult([4,3,2,1]))

n = [4,3,2,1]
print(reduce(lambda x,y: x*y, n))
