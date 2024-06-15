# Vowel Checker

This is a simple Python script to check if a given letter is a vowel.

## Description

The script defines a function `isVowel` which takes a letter as an argument and prints whether the letter is a vowel or not. It then demonstrates the use of this function with a few examples.

## Code

```python
def isVowel(letter):
  if letter in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
    print("Letter passed is a vowel letter.")
  else:
    print("Letter passed is not a vowel letter.")

isVowel("a")
isVowel("C")
isVowel("E")
