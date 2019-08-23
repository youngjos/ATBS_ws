def returnEmptyString():
    return ''

def div42by(divideBy):
    try:
        42/divideBy
    except ZeroDivisionError: # runs if division by zero
        print('Error: you cannot divide by 0!') 
        # return None
    except: # runs if another error occurse
        print('Error: unspecifed')
        # return None
    else: # runs if no error
        print('No error raised!')
        return 42/divideBy
         
print(div42by(0)) # ZeroDivisionError
print(div42by('six')) # TypeError, not specified will go to unspecified except block
print(div42by(2)) # no error, will go to else block


