"""
Lambda function
https://www.youtube.com/watch?v=Ob9rY6PQMfI

"""

"""Basic easy one-line function""" 
add5 = lambda x : x+5
print(add5(7))

square = lambda x : x*x
print(square(2))

get_tens = lambda p : int(p/10)%10
print(get_tens(456))


"""Lambda as an argument in other functions (most common)"""

# Sorting a List of Tuples
list1 = [('eggs', 5.25), ('honey', 9.70), ('carrot', 1.10), ('peach', 2.45)]
list1.sort(key = lambda x: x[0])
print(list1)

# Sorting a List of Dictionaries
list1 = [{'make':'Ford', 'model': 'Focus', 'year':2020}, {'make':'Tesla','model':'X','year':2011}]
list2 = sorted(list1, key = lambda x:x['year'])
print(list2)

# Filtering a List of Integers using Lambda
list1 = [1,2,3,4,5,6]
list2 = list(filter(lambda x:x%2==0, list1))
print(list2)

odd = lambda x:x%2 == 1
list1 = [1,2,3,4,5,6]
list2 = list(filter(odd, list1))
print(list2)


"""Lambda Function on a List using Map"""

# Map: apply the lambda function to every element in this list
list1 = [1,2,3,4,5,6]
list2 = list(map(lambda x:x ** 2, list1))
print(list2)


"""Lambda Conditional"""

# lambda args: a if condition_eexpression else b
start_with_J = lambda x: True if x.startswith('J') else False
print(start_with_J('Joey'))

wordb4 = lambda s,w : s.split()[s.split().index(w)-1] if w in s else None
sentence = 'Four score and seven years ago'
print(wordb4(sentence, 'seven'))


"""Lambda on DateTime Objects"""
import datetime

now = datetime.datetime.now()
print(now)
year = lambda x:x.year
print(year(now))


"""Functional Programming"""
def do_something(f, val):
    return f(val)
 
func = lambda x: x**3
print(func(16))
print(do_something(func,5))

 
"""Extreme Lambdas"""
isnum = lambda q:q.replace('.','',1).isdigit() or (q.startswith('-') and q[1:].isdigit())
print(isnum('25934'))
print(isnum('3.2352'))
print(isnum('T33'))
print(isnum('-16'))

is_num = lambda r: isnum(r[1:]) if r[0]=='-' else isnum(r)
print(is_num('-16.4'))

tonum = lambda s:float(s) if is_num(s) else -1
print(tonum('30y'))
print(tonum('-21.67'),type(tonum('-21.67')))