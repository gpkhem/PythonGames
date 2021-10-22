"""def div42by(divideBy): #function being defined
    try:
        return 42 / divideBy #return the value
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2)) # printing its arguments that are given
print(div42by(12))
print(div42by(0))
print(div42by(1)) """


print('How many dogs do you have?')
numDogs = input()
try:
    if int(numDogs) >= 3:
        print('You crazy, thats alot')
    else:
        print('That\'s not that much')
except ValueError:
    print('C"mon dude, put a number')
