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
# blank string is Falsey, all others are Truthy
# 0 and 0.0 are Falsey, all others are Truthy
# bool() function returns a True or False value based on the Truthy and Falsey state of the argument