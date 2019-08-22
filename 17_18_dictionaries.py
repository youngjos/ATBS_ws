# key value pair in dictionaries

myCat = {'size' : 'fat', 'color' : 'gray', 'disposition' : 'loud'}
print(myCat)
print(myCat['size']) # grab key value

# order does not matter for dictionaries, however in lists it does
print([1,2,3] == [3,2,1]) # false
elizabethsCat = {'color' : 'gray', 'size' : 'fat', 'disposition' : 'loud'}
print(myCat == elizabethsCat) # true

# myCat['favorite food'] KeyError

print('size' in myCat) # like lists and strings

# functions
print(list(myCat.keys())) # a list of the keys
print(list(myCat.values())) # a list of the values
print(list(myCat.items())) # returns a list of tuples which are lists using parantheses that cannont be changed (immutable)

for desc in myCat.keys():
    print(desc)

print(myCat.get('size', 0)) # 'fat' since 'size' exists as a key
print(myCat.get('favorite food', 0)) # 0 since 'favorite food' does not exist as a key and falls back to the second arg

myCat.setdefault('favorite food', 'lasagna')
print(myCat['favorite food']) # though 'favorite food' doesnt exist in the dictionary the default gives a fall back 

# character counter prog
message = 'It was a bright cold day in April.'
count = {}

for char in message:
    count.setdefault(char, 0) # sets the default of each char to 0
    count[char] += 1 # adds one each time it comes across that character to that character key

print(count)

import pprint
pprint.pprint(count) # pretty print

countString = pprint.pformat(count) # formats it as a string
print(countString)

# type method
print(type(32))
print(type(True))
print(type('blah'))
print(type(myCat))