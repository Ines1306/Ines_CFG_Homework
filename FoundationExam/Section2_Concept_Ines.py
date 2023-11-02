# 2.1

class InvalidInput(Exception): # for question 2.2
    pass

def is_isogram(word):
    if type(word) is not str:
        raise InvalidInput("Input must be a string")
    try:
        word = word.lower() # we have to add this so than "A" is equal to "a" for example
        for letter in word:
            if word.count(letter) > 1: # since if the letters are repeated than it is not a isogram
                return False
        return True
    except TypeError: # for integer inputs for example
        raise InvalidInput("Input must be a string")

# print(is_isogram("isogram")) # It prints True as expected
# print(is_isogram("uncopyrightable")) # It prints True as expected
# print(is_isogram("ambidextrously")) # It prints True as expected
# print(is_isogram("anaconda")) # It prints False as expected
# print(is_isogram("Ana")) # It prints False as expected


