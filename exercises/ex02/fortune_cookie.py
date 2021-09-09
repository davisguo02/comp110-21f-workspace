"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730430788"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

cookie: str = ("Your fortune cookie says...")
vibes: str = ("Now, go spread positive vibes!")

if randint(1, 3) == 1:
    print(cookie)
    print("You will make good grades this year!")
    print(vibes)
else:
    if randint(1, 3) == 2:
        print(cookie)
        print("You will pass COMP110.")
        print(vibes)
    else: 
        if randint(1, 3) == 3:
            print(cookie)
            print("You will fail COMP110.")
            print(vibes)
