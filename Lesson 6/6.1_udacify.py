# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'

def udacify(s):    
    return 'U' + s



print(udacify('dacians'))
#>>> Udacians

print(udacify('turn'))
#>>> Uturn

print(udacify('boat'))
#>>> Uboat
