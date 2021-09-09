"""Counting letters in a string."""

__author__ = "730430788"


# Begin your solution here...

search: str = input("What letters do you want to search for?: ")
word: str = input("Enter a word: ")

i: int = 0
counter: int = 0

while i < len(word):
    if word[i] == search:
        counter = counter + 1
        i = i + 1
    else: 
        i = i + 1

print("Count: " + str(counter))