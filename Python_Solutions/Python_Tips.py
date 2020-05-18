
# 10 Python Tips and Tricks For Writing Better Code
# https://www.youtube.com/watch?v=C-gEQdGVXbk

""" 1. Condition """ 
condition = True

# Before
if condition:
    x = 1
else:
    x = 0

##### After (Ternary Conditionals)
x = 1 if condition else 0

print(x)


""" 2. Large Number Easier to Read"""
# Before
num1 = 1000000000000
num2 = 1000000000
total = num1 + num2
print(total)

##### After (Underscore Placeholders)
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f'{total:,}')


""" 3. Context Managers """
# Managing Files / Threads / Locks / DB connections

# Before
f = open('test.txt', 'r')
file_content = f.read()
f.close()

##### After (No need tp manage resoure yourself)
with open('test.txt', 'r') as f:
    file_content = f.read()

words = file_content.split('')
word_count = len(words)
print(word_count)


""" 4. Enumerate """

names = ['Coney', 'Chris', 'Dave', 'Travis']

for index, name in enumerate(names):
#for index, name in enumerate(names, start = 1):
#for index, name in enumerate(names[1:]):
    print(index, name)


""" 5. Loop Over 2 Lists at Once """

# Itertool module

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spider Man', 'Super Man', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')


""" 6. Unpacking """

a, b = (1, 2)
print(a)
print(b)

# Underscore (Variable not using anywhere else)
a, _ = (1, 2)
print(a)

# c to the rest of the values
# return c as a list
a, b, *c = (1, 2, 3, 4, 5)

# hide the rest of the tuple
a, b, *_ = (1, 2, 3, 4, 5)

# middle 2
a, b, *c, d= (1, 2, 3, 4, 5)

# get the last one
a, b, *_, d= (1, 2, 3, 4, 5, 6, 7)


""" 7. Setattr() & Getattr() """
class Person():
    pass

person = Person()

first_key = 'first'
first_value = 'Evan'

##### After
setattr(person, 'first', 'Evan')
#setattr(person, first_key, first_value)
print(person.first)

first = getattr(person, first_key)
print(first)


person_info = {'first': 'Corney', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))



""" 8. GetPass """

# Hide input password
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

print('Logging In...')


""" 9. Python dash m """
# In command line
# Creating vertual environment
# python -m venv my_env

# Running the module after '-m'
# The module that not existing in current dir
# Search in sys.path for that file and run it



""" 10. Help / Dir """

# Find more information

import smtpd
help(smtpd)

from datetime import datetime
dir(datetime)