"""Repeating a beat in a loop."""

__author__ = "730430788"


# Begin your solution here...

counter: int = 0
end: int = 1

repeat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it?" ))



if number <= 0:
    print("No beat...")
else:
    while counter < end:
        print((repeat + " ") * (number - 1) + (repeat))
        counter = counter + 1



