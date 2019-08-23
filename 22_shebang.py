#! python3
# that is the shebang line used for specifying the version of python when running a python script

print('Hello world!')

# %* passes through cmd args into python
# @py runs python
# @pyw runs python windowless
# @pause hangs the windows until a close key is executed
# you can add a script file path to PATH to make things easier to run from win+r or the cmd line
# for example running [22_shell_script arg1 arg2 ... argN] will work if the file path was added to PATH 

import sys
print(sys.argv) # prints file path and all of the arguments in a list