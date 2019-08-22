# Many things you can do with strings you can do with lists

name = 'Josh_Young'
print(name[0]) # J
print(name[0:3]) # Jos
print(name[5:]) # Young
print(name[:4]) # Josh
print(name[-1]) # g
print('Josh' in name) # True
print('Alexander' in name) # False
for letter in name:
    print(letter)

# string in python are immutable and must be remade
# name[4] = 'x' ERROR

# lists are mutable meaning you can change the single indexes

spam = 42
cheese = spam # value assignment, not a reference to spam
spam = 84
print(cheese)

spam = [0, 1,  2, 3] # spam is just a reference to the list
cheese = spam # lists are reference assigned, meaning cheese is assigned to the reference of spam, which is reference to the list
cheese[1] = 'Hello' # updates spam and cheese because referring to the same list reference
print(spam)
print(cheese)

# all mutable values are references

def eggs(aList):
    aList.append(4) # local reference in the scope of only the function

eggs(spam) # since it is a reference the spam global variable will change
print(spam)

# references are computationally cheap since they are just references to data and not re-copying the data

import copy
ham = copy.deepcopy(spam) # copies the list fully, not as a reference
ham.append(5)
print(spam)
print(ham)

breakfast = ['eggs',
              'apples']  # lists can do line continuation by default

beans = ('bush\'s' + \
' baked') # line continuation character allowing for less ugly code, MAKE SURE THESE NO WHITE SPACE AFTER THE \

print(beans)