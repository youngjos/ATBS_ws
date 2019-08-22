password = 'swordfish'
if password == 'swordfish':
    print('access granted')
else:
    print('wrong password')

name = 'Bob'
age = 3000
if name == "Alice":
    print('Hi Alice')
elif age < 12: # else if
    print('Your too young to be Alice.')
elif age > 2000:
    print('You undead monster!')
elif age > 100:
    print('Your too old to be Alice.')

# Truthy and Falsey values
# Blank string is falsey, all others are truthy
# 0 and 0.0 are falsey, all others are truthy
# bool() function returns a true or false value based on the truthy and falsey state of the argument