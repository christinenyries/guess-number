import random
from functools import wraps


def computer_says(*args, **kwargs):
    print(f"{'COMPUTER':10}: " + "".join(args), **kwargs)


def user_says(*args, **kwargs):
    return input(f"{'USER':10}: " + "".join(args), **kwargs)


def guess(n):
    """Asks user to guess a random number from 1 to `n`.

    Args:
        n (int): The highest possible number to be guessed

    """
    random_number = random.randint(1, n)
    guess = 0

    computer_says("Nice. I've thought of a number. Please guess it.")

    while guess != random_number:
        guess = int(user_says("My guess is "))
        if guess > random_number:
            computer_says("Your guess is too high. Guess again.")
        elif guess < random_number:
            computer_says("Your guess is too low. Guess again.")

    computer_says(f"Yes, it's {random_number}. You guessed the number I had in mind.")


def computer_guess(n):
    """Asks computer to guess a random number from 1 to `n`.

    Args:
        n (int): The highest possible number to be guessed

    """
    computer_says("Let me guess this time.")

    low = 1
    high = n
    feedback = ""

    while feedback != "c":
        guess = random.randint(low, high)
        computer_says(
            f"Is it {guess}? "
            + "Please enter (H) if too high, (L) if too low, or (C) if it's correct."
        )
        feedback = user_says("It's ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    computer_says(f"The number you're thinking of is {guess}!")
    computer_says("Thank you for playing with me.")


if __name__ == "__main__":
    computer_says("Let's play a number guessing game.")
    n = int(user_says("Okay. Let's take turns in guessing a number from 1 to "))
    guess(n)
    computer_guess(n)
