## 6 while loops
spam = 0
while spam < 5: # typical while loop
    print("Hello World!")
    spam = spam + 1

name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break # breaks the loop
print('Thanks!')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # jumps to top of loop so 3 never gets printed
    print(spam)

## 7 for loops
for i in range(5): # number from 0 to arg exclusive
    print(str(i))

# range(inclusive, exclusive, increment)