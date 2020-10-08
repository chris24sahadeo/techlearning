#  https://www.youtube.com/watch?v=H1elmMBnykA&t=13s  

#  triple quotes so you don't need to escape
string = '''"I am awesome," said Chris' friend.'''
print(string)

# ternary operatory
answer = 10 if 3 + 5 == 10 else None
print(answer)

# raw strings ignore escape sequences
print(r'Hello, World!\n')

# iterators
list = range(10)
itr = iter(list)
print(next(itr))
print(next(itr))
print(next(itr))

# dicts
thesaurus = {
  'happy': ['elated', 'extatic'],
  'sad': ['down', 'meloncholy']
}
print(thesaurus['sad']) 
for word in thesaurus:
  print(word)

# args and kwargs
# https://www.geeksforgeeks.org/args-kwargs-python/


# lambda functions
# https://realpython.com/python-lambda/
add = lambda x, y: x + y
print(add(2, 6))

square = lambda x: x**2
print(square(56))

# map, reduce, filter on arrays
print((map(lambda x: x*2, range(5))))
print(filter(lambda  x: x%2 == 0, range(11)))
print(reduce(lambda x, y: x+y, range(1,4)))

# threading

# regex
import re

if re.search('chris', 'chris is batman'):
  print(True)

# databases (will return to this later after the SQL tutorial)