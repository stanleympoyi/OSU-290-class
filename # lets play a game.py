# lets play a game

import random

print('Hello, what is your name?')
name = input()

secretNumber = random.randint(1,20)
print('well '+ name + ', i am thinking of a number between 1 and 20')

#Ask the player to guess 6 times

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print('Try again,your guess is too low.')
    elif guess > secretNumber:
        print('Try again, your guess is too high.')
    else:
        break  # This Conditions is a Correct Guess!
    
if guess == secretNumber:
                        print('Good job, ' + name + '! you guessed my number in ' + str (guessesTaken) + ' guesses')
else:
     print('Nope the number I was thinking of was ' + str(secretNumber))
        
        
    
