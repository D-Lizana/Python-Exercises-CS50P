# In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str,
#  converting any codes (or aliases) therein to their corresponding emoji.
# need to pip install emoji

import emoji

prompt = input("Input: ")

print(f"Output: {emoji.emojize(prompt)}")