import random


def play():
    while True:
        computer_choice = random.choice(['r', 'p', 's'])
        user_choice = input("Press 'r' for Rock, 'p' for Paper and 's' for Scizor:")

        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r')\
                or (user_choice == 's' and computer_choice == 'p'):
            print('You Won!')
        else:
            print('You lost!')

        if input("Wanna play again? [Y/N]:") in 'nN':
            break


play()
