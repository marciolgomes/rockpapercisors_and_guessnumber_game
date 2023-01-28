import random
import time


def guess(x):
    guess_number = x
    computer_list = []
    computer_guess = 0
    while computer_guess != guess_number:
        computer_guess = random.randint(1, 20)
        if computer_guess not in computer_list and computer_guess != guess_number:
            print(f"It isn't {computer_guess}? Im trying...")
            computer_list.append(computer_guess)
            time.sleep(2)

    print(f'Found it! The number is {guess_number}!')


guess(int(input('Insert a secret number from 1 to 20: ')))
