"""
Map function:
    - Apply the same function to each element of a sequence
    - Return the modified list
"""

def square(lst1):
    lst2 = []
    for num in lst1:
        lst2.append(num **2)
    return lst2

print(square([4,3,2,1]))

n = [4,3,2,1]
print(list(map(lambda x: x**2,n)))
# Same thing
print(list(map(square,n)))
