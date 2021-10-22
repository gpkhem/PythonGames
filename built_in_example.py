# Writing your own functions
""" def hello():
    print('Show me once')  #body of the function
    print('Show me twice')
    print('Show me thrice')

hello() """

"""def hello(name): # theses are parameters
    print('Show me ' + name)  #body of the function

hello('Geter') # these are arguments
hello('Jerry') """

""" def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber) """

#Global and Local Scope
"""spam = 42 # global scope

def eggs():
    spam = 42 # local variable

print('some code here.')
print('some more code.') """

def spam():
#    global eggs # using the eggs = 42 even though its within local variable
    eggs = 'Hello' #local variable
    print(eggs) # local variable

eggs = 42 #global variable
spam() # callin the function at the top
print(eggs) #global variable
