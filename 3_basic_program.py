#exec starts at top and goes down

print('Hello World') # prints to console
# func(args)

print('What is your name?')
myName = input() # takes name as input
# waiting for keyboard input from console
print('It is good to meet you, ' + myName) 

print('The length of your name is: ')
print(len(myName)) # len function gets size of string
print('What is your age?')
myAge = input() # takes age as input
print('You will be ' + str(int(myAge) + 1) + ' in a year.')