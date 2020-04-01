"""
Filter
    - Pass in a condition
    - filter the lsit based on the condition
"""
def over_two(lst1):
    lst2 = [x for x in lst1 if x>2]
    return lst2

print(over_two([4,3,2,1]))

n = [4,3,2,1]
print(list(filter(lambda x:x>2, n)))

