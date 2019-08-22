spam = ['hello', 'howdy', 'hi', 'hey']
print(spam.index('hello'))

# print(spam.index(undefined)) will raise an exception
spam = ['hello', 'howdy', 'hi', 'hey', 'hello']
print(spam.index('hello')) # will always give the first occurence

spam.append('whats up') # adds it at the end
print(spam)

spam.insert(1, 'heya') # add it at the given index, such as 1 in this case
print(spam)

# print(spam.remove(undefined)) will raise an exception
spam.remove('heya')
print(spam)

spam.remove('hello') # only removes the first occurence
print(spam)

eggs = [1, 4, 3 ,7 , 0] # sorts in numerical order
eggs.sort()
print(eggs)

ham = ['b', 'c', 'a', 'B'] # sorts in ASCII-betical order, meaning uppercase before lowercase
ham.sort()
print(ham)

ham.sort(key=str.lower) # sorts it in true alphabetical, with uppercase taking precedence 
print(ham)