# Rock, Paper, Scissors game.
# Import modules
import sys
import random
import time

# Scores
wins = 0
loses = 0
ties = 0

# Strikes
strikes = 0
balls = 0
fouls = 0

# Agreements
yes = ('y', 'yes')
no = ('n', 'no')


# Are we
# playing?
def Play():
    global wins
    global loses
    global ties

    # What are our options?
    options = ('rock', 'paper', 'scissors')

    playing = 'y'

    while playing in yes:

        # Users and their choices
        human = input('Choose between \'rock\', \'paper\' or \'scissors\': ').lower()
        computer = random.choice(options)

        # Wrong choice?
        while human not in options:
            print('\nYo! That\'s not a word I asked for.')
            Strike()
            human = input('Choose between \'rock\', \'paper\' or \'scissors\': ').lower()

        # Say 'ROCK, PAPER SCISSORS!'
        for n in options:
            print('\n', n.upper(), '!', sep='')
            time.sleep(.3)

        # Print users choices
        print('\nYou picked:', human.upper())
        print('Computer picked:', computer.upper())

        # Testing results:

        # Same choice?
        if human == computer:
            print('\nIt is a tie!')
            ties += 1
        # Human loses?
        elif (human == options[0] and computer == options[1]) or (human == options[1] and computer == options[2]) or (
                human == options[2] and computer == options[0]):
            print('\nYou lose!')
            loses += 1
        # Human wins?!
        elif (human == options[0] and computer == options[2]) or (human == options[1] and computer == options[0]) or (
                human == options[2] and computer == options[1]):
            print('\nYou win!')
            wins += 1

        # Prints Total Results
        print('\nTotal wins:', wins)
        print('Total loses:', loses)
        print('Total ties:', ties, '\n')

        PlayAgain()


# Whas is PlayAgain()?
def PlayAgain():
    global yes
    global no

    # Play again?
    playing = input('Would you like to play again?(y/n): ')

    # YAY! :D
    while playing in yes:
        print()
        Play()

    # NAY! :(
    if playing in no:
        print('\nThanks for playing!')
        sys.exit()

    # Lol, WAT?
    else:
        Strike()


# What is Strike()?
def Strike():
    global strikes

    # This is a strike
    strikes += 1

    while strikes <= 3:

        # Indeed it is...
        print('\nThat\'s strike', strikes, '\n')

        # Strike 3!
        if strikes == 3:
            print(strikes, 'strikes! YOU\'RE OUT!')
            sys.exit()

        PlayAgain()

    print()


# Can we FINALLY play?
Play()
