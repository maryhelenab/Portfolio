#!/usr/bin/env python3
"""Simple Caesar Cipher Program."""

import string

def main():
    """Run Caesar cipher program.""" 
    shift = 3
    letters = string.ascii_letters + string.punctuation + string.digits
    choice = input("would you like to encode or decode?")
    word = input("Please enter text")
    encoded = ""

    if choice == "encode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                new_index = letters.index(letter) + shift
                encoded += letters[new_index]
    elif choice == "decode":
        for letter in word:
            if letter == " ":
                encoded += " "
            else:
                new_index = letters.index(letter) - shift
                encoded += letters[new_index]
    print(encoded)

if __name__ == "__main__":
    main()
#Put all logic inside a function.
