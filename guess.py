from random import randint

def main():
    '''Guessing game from Teach Yourself Python in 24 Hours'''
    print("Welcome to the number guessing game!")
    number = randint(1,10)
    while True:
        guess = input("Guess a number between one and ten. Type 'q' to quit: ")
        if guess == 'q':
            break
        if int(guess) == number:
            print("That's right!")
            break
        else:
            print("That's not right. Sorry! Guess again.")

if __name__ == '__main__':
    main()


        