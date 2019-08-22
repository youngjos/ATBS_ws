spam = 42 # global scope
ham = 32

def eggs():
    spam = 24 # local scope to eggs, wont exist after function return

def bacon():
    print(ham) # will use the global ham variable so 32

def baconButLocal():
    ham = 64
    print(ham) # will use the local ham variable so 64

def baconButLocalButUsingGlobal():
    global ham # tells function to refer to the ham in the global scope 
    ham = 128 # redefines the global ham

bacon()
baconButLocal()
baconButLocalButUsingGlobal() # redefines ham since it used the global keyword
print(ham)

