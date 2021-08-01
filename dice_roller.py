# things to do:
# 1. get user input of how many sides are on the die (x)
#     make sure user inputs a number only. if loop. (x)
# 2. implement random to pop out the random number on the die
# 3. print out the answer
# 4. ask user to roll again. if yes, loop program. else quit.
import random
def dice_roller():

# ask user how many sides are on the die
    print('How many sides are on your die?')
# takes in input from user
    input_u = input()

# prints input
    print('you selected a', end = ' ')
    print(int(input_u), end = ' ')
    print('sided die.')
# random is used from range 1 to input_u
    random.randint(1, int(input_u))

# print random int
    print('Your result is:', end = ' ')
    print(random.randint(1, int(input_u)))

# asks user if they want to roll again
    print('Roll again? yes or no')
    input_i = input()

# if yes, return to play again
    if input_i == 'yes':
        dice_roller()
    else:
        print('thanks for playing.')
        exit()

# if no, close
dice_roller()