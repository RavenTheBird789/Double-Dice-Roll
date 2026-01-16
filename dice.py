# Dice Roll

import random
from random import randint

def green(text: str) -> str: 
    # Wrap text in ANSI codes for green color
    return f"\033[92m{text}\033[0m"

def red(text: str) -> str:
    """Wrap the given text in red color codes for terminal display."""
    return f"\033[91m{text}\033[0m"

max = 12
val = range(2, max+1)
dec = random.choice(val);
print(f"Decision for minimum value: {dec}\n");

def roll():
    die_1 = range(1, 6)
    die_2 = range(1, 6)

    roll_die1 = random.choice(die_1)
    roll_die2 = random.choice(die_2)
    total = (roll_die1 + roll_die2)
    
    print("Roll 1:")
    print(f"Die 1: {roll_die1}")
    print(f"Die 2: {roll_die2}")
    print(f"You total for the Dice Roll is: {total}")
    
    if total >= dec:
        print(green("Congratulations!\n"))
    else:
        print(red("Sorry, you lost.\n"))
roll();

def roll_2():
    die_1 = randint(1, 6)
    die_2 = randint(1, 6)
    total = (die_1 + die_2)

    print("Roll 2:")
    print(f"Die 1: {die_1}")
    print(f"Die 2: {die_2}")
    print(f"You total for the Dice Roll is: {total}")

    if total >= dec:
        print(green("Congratulations!\n"))
    else:
        print(red("Sorry, you lost.\n"))
roll_2();
