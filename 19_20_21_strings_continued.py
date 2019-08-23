# python can do more than just adding strings 
'Hello' # a string
"Hello" # also a string

# escape characters
print('I\'m using escape characters!')
# list of escape characters
# \' single quotes
# \" double quote
# \t tab
# \n newline
# \\ backslash
# there are other escape characters not listed here

# raw string
print(r'That is Carol\'s cat.') # escape escape characters

print('''This is a
multi-line string''')

spam = 'Hello world!'
print('Hello' in spam) # this works like in lists
print('HELLO' in spam) # case sensitive

# strings are immutable so string methods return a entirely new string
print(spam.upper()) # you would have to do spam = spam.upper()
print(spam.lower()) # upper and lower are useful for 'standardizing' string input
print(spam)

lowerCase = 'i am all lower'
upperCase = 'I AM ALL UPPER'
print(lowerCase.islower()) #  all characters must be lower or upper to return true for islower() and isupper() respectivley, strings w/o characters will return false for both
print(upperCase.isupper())
print(upperCase.islower())

# other string methods
# isalpha() - letters only
# isalnum() - isalphanumeric - letters and numbers only
# isdecimal() - numbers only
# isspace() - whitespace only
# istitle() - titlecase only
# startswith(string) - checks if a string starts with the arg string
# endswith(string) - checks if a string ends with the arg string
# string.join(listOfStrings) - puts the string in between each string in the listOfStrings arg
# string.split(aString) - splits string at each occurence of the aString arg, space by default
# string.l/rjust(n, str) - forces a string to be a certain length n forcing in str, space by default
# string.center(n, str) - forces a string to be a certain length n forcing in str, space by default
# strip(), lstrip(), rstrip() - removes white space or a given string from a string
# string.replace(a, b) - replaces all instances of a in string with b
print('Hello world!'[5].isspace()) # True
print('This Is Title Case'.istitle()) # True
print(', '.join(['cats', 'rats', 'bats'])) # string.join(listOfStrings) puts the string in between each string in the listOfStrings arg
print('My name is Simon'.split()) # splits at spaces
print('My name is Simon'.split('m')) # splits at 'm's 

print('Hello'.ljust(10)) # forces characters from the right until the length of the string is 10, space by default
print('Hello'.rjust(10, '.')) # forces characters from the left until the length of the string is 10, space by default, in this case .
print('Hello'.center(10, '.')) # forces characters from the left and right until the length of the string is 10, space by default, in this case .
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS')) # strip goes in on the left and right but not center

spam = 'Hello there!'
print(spam.replace('e', 'XYZ'))

import pyperclip
pyperclip.copy('I am copying this to my computers clipboard!')
# pyperclip.paste() will paste the clipboard

name = 'Alice'
place = 'Main Street'
time = '6 PM'
food = 'turnips'

# string formatting using conversion factors
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.'% (name, place, time, food))