# Dragons and Dungeons

from random import randint
from time import sleep
# Modules imported
def intro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.\n''')
def choose():
    choice = input('Which cave will you go into? (1 or 2) : ')
    while (True):
        if choice == '1' or choice == '2':
            break 
        else:
            print('Invalid choice! Choose either cave 1 or cave 2.')
            choice = input('Which cave will you go into? (1 or 2) : ')
    return choice
def progress(choice):
    destiny = str(randint(1,2))
    print(f'You approach the cave {choice}...')
    sleep(2)
    print('It is dark and spooky...')
    sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...\n')
    sleep(2)
    if choice == destiny:
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')
def repeat():
    playagain = input('Wanna play again? [Y/n] : ')
    return playagain
def main():
    while (True):
        intro()
        choice = choose()
        progress(choice)
        playagain = repeat()
        if playagain not in ['','y','Y']:
            break
    print('Hope to see you again!')
if __name__=='__main__':
    main()
# end of game
