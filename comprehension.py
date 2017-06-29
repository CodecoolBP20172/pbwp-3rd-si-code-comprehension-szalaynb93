"""
This programs funkctions as an AI which is getting a random number between 1 and 20.
The user's task is to guess this number from maximum 6 guesses. The AI gives a hint after every guess.
"""    

import random # Inporting the random module.

guessesTaken = 0 # Variable which shows the number of guesses the user already taken.

print('Hello! What is your name?') # Output : asks the user's name.
myName = input() # Variable, waiting for the user's input, his or her name.

number = random.randint(1, 20) # This is the variable which is responsible for the random integer between 1 and 20.
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # Gives an output to the user about the previous process.

while guessesTaken < 6: # It's a loop which works only until we took 6 guesses (or we give the correct anwser)
    print('Take a guess.') # Asks the user for input.
    guess = input() # This variable equals to the given input.
    guess = int(guess) # The program declares that it waits for and integer. If it's a string it raises ValueError.

    guessesTaken += 1 # The user used one guess so it adds one to the global variable.

    if guess < number: # The program give a hint. If the guessed number is smaller than the program's number then do the following:
        print('Your guess is too low.') # Gives the information above to the user.

    if guess > number: # If the the guessed number is smaller than the program's number then do the following:
        print('Your guess is too high.') # Gives this information to the user.

    if guess == number: # If the guess is correct do the following:
        break # Break the while loop.

if guess == number: # If the guess is correct, do the following:
    guessesTaken = str(guessesTaken) # This variable casts it's type to string in order to put it in the next line easily.
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # The program gives compliments to the user.

if guess != number: # If the last guess is incorrect, do the following:
    number = str(number) # It casts itself to string type.
    print('Nope. The number I was thinking of was ' + number) # The program gives the opportunity to say unsophisticated things...
