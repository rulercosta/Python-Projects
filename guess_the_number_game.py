#Guess The Number Game

from random import randint
# random module to generate random integer between 1 and 10
secret_num = randint(1,10)
num_of_guesses, max_guesses = 0, 3
# globally declared variables to control flow of program
def hello():
    name = input('Hello! What should I call you? : ')
    choice = input(f'Nice to meet you {name}! Wanna guess the number hidden here \'##\' ? [Y/n]: ')
    if choice != 'Y' and choice != 'y' and choice != '':
        print(f'Hope to see you again {name}.')
        return EXIT
    print('Here\'s a hint: the secret number lies between 1 and 10.')
    return name
# name input and greeting ends
def guess_num():
    global secret_num, num_of_guesses, max_guesses
    num_of_guesses += 1
    while (num_of_guesses <= max_guesses):
        guessed_num = input(f'Guess no. {num_of_guesses}: ')
        # error handling for guessed number
        while (True):
            try:
                guessed_num = int(guessed_num)
            except ValueError:
                print('Input is not an integer! Try again.')
                guessed_num = input(f'Guess no. {num_of_guesses}: ')
            else:
                break
        # end of error handling
        if guessed_num < secret_num:
            print('Your guess is too low')
        elif guessed_num > secret_num:
            print('Your guess is too high')
        else:
            break
        num_of_guesses += 1
        # loop ends
# guess number logic ends
def final_message(name):
    global secret_num, num_of_guesses, max_guesses
    if num_of_guesses <= max_guesses:
        print(f'Congrats {name}! You guessed my number {secret_num} in {num_of_guesses} guesses!!')
    else:
        print(f'Nope! I was thinking of {secret_num}.')
# final message ends
def main():
    name = hello()
    guess_num()
    final_message(name)
# main module ends
if __name__ == '__main__':
    main()
#End of Game
