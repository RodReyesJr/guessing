from random import randint
import time

def main():
    '''Guessing game from Teach Yourself Python in 24 Hours'''
    print("Welcome to the number guessing game!")
    number = randint(1,10)
    maxguess = 5 # max guess count allowed
    numguess = 0 # guess counter
    while True:
        guesses = input("Guess a number between one and ten. Type 'q' to quit: ")
        # Error prevention doesn't seems to work        
        try: 
            if guesses == 'q':
                break         
            guess = int(guesses)
            if int(guess) == number:
                print("That's right!")
                time.sleep(3) # delay for awhile
                break
            elif int(guess) > number:
                print("That's not right. Too high! Sorry! Guess again.")
                numguess = numguess + 1
            elif int(guess) < number:
                print("That's not right. Too low! Sorry! Guess again.")
                numguess = numguess + 1

            if numguess == maxguess:
                break # quit now if maximum guess is reached
        except ValueError:
            print("\nPlease enter a number between 1 to 10. Press 'q' to quit.")

if __name__ == '__main__':
    main()


        