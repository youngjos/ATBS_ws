def helloWorld(): # def for making functions
    print('Hello World!')

helloWorld()

def helloName(name):
    print('Hello ' + name + '!')

helloName('Josh')

def plusOne(number):
    return number + 1 # all functions have a return, default None

print(plusOne(5)) 

# print mods

print('Hello', end=', ') # overrides default end which is \n
print('World')
print('cat', 'dog', 'mouse', sep='HAM') # overrides default seperator which is ' ' (a space)


