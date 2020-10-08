'''
The god of beautiful python: Raymond Hettinger

Transforming Code into Beautiful, Idiomatic Python:
- https://www.youtube.com/watch?v=UANN2Eu6ZnM&t=2809s
- https://github.com/abrenaut/python-cheat-sheet
- https://www.youtube.com/watch?v=OSGv2VnC0go&list=PLRVdut2KPAguz3xcd22i_o_onnmDKj3MA&index=3
'''

for i in range(5):
  print(i**2)

colors = ['red', 'blue', 'green']
for color in colors:
  print(color)

for i in reversed(colors):
  print(i)

for i, color in enumerate(colors):
  print('{} {}'.format(i, color))

names = ['chris', 'jen', 'bob']
for name, color in zip(names, colors):
  print('{} {}'.format(name, color))

for color in sorted(colors):
  print(color)

# comparison functions

# for else

# dictionaries
dictionary = {
  'batman': 'Bruce Wayne',
  'superman': 'Clark Kent'
}

for key in dictionary:
  print(key)

# use dictionary.keys() only when we need to mutate

for k, v in dictionary.items():
  print(k, v)

d = dict(zip(names, colors))
print(d)

# Stopped @ 26:46
