# lists with item
spam = ['cat', 'bat', 'rat', 'elephant'] # comma delimited
print(spam[0]) # arrays start at 0, cat
print(spam[-1]) # elephant
print(spam[-2]) # rat

ham = [['cat', 'bat'], ['car', 'bike']]
print(ham[1][0]) # car

# slicing
print(spam[1:3]) # list[inclusive, exclusive]

spam[1:3] = ['CAT', 'DOG', 'MOUSE'] # replacing a slice with a whole new list, index 1 inclusive, 3 exclusive
print(spam)

# "cut off" slicing
# slices has two indexs, the new list items start at the first index and go up to but dont include the second index
print(spam[:2]) # same as spam[0:2]
print(spam[3:]) # the list starting at index 3 inclusive

del spam[1]
print(spam)

print(len(spam))

eggs = [1,2,3] + [4,5,6] # list combining
print(eggs)
print(eggs * 3)
# ops on lists are similar to ops on strings

print(list('HELLO')) # listifying

print(5 in eggs) # True
print(7 in eggs) # False

for egg in eggs:
    print(egg)

print(list(range(0,4)))

supplies = ["pens", "staples", "tape"]

for stuff in range(len(supplies)): # will go number of times the lenth of the list, starting at 0 going to len-1 
    print('Index ' + str(stuff) + ' in supplies is: ' + supplies[stuff])

cat = ['fat', 'orange', 'loud'] # I'm sorry Jon

size, color, disposition = cat # multiple assingment using lists
print(size)
print(color)
print(disposition)

a, b = 'AAA', 'BBB' # multiple assignment using commas
a, b = b, a # swap
print(a)
print(b)

bacon = 42
bacon += 1 # works also with - * / % and are shorthand for: var = var op num
print(bacon)