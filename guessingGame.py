#Guess the number game
import random

print('What they call you')
name = input()

print('Well, ' + name + ' what number you think i got?')
secretNumber = random.randint(1,20)

for guessesTaken in range(0,5):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #this condition is for the correct guess

if guess == secretNumber:
    print('You did it ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guess')
else:
    print('Naw, I was thinking ' + str(secretNumber))


# print('You took ' + str(guessesTaken) + ' guesses')
