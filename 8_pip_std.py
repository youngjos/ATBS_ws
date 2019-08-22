# python has a stdlib

# such as random
import random # used to use functions from random
spam = random.randint(1, 10) # library.function(args)
print(spam)

# you can use pip to get third-party modules such as pyperclip
import pyperclip
pyperclip.copy('copy copy copy')
print(pyperclip.paste())