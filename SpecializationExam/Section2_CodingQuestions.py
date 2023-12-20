# 2.1
# A

from collections import Counter

def unique_conso(s):
    vowels = 'aeiou' # Define what letters are vowels
    s_lower = s.lower() # lowercase the input string

    count_unique_consonant = Counter(char for char in s_lower if char not in vowels)
    unique_consonant = [key for key, value in count_unique_consonant.items() if value == 1]
    # we use .items to check what's inside the count_unique_consonant, which is a dictionary
    # we check the consonants that only have a count of 1, thus being unique
    # this will result in a list with each unique consonants

    return len(unique_consonant)

# Tests

print(unique_conso("cat")) # It results in 2
print(unique_conso("cataract")) # It results in 1
print(unique_conso("ines")) # It results in 2
print(unique_conso("joao")) # It results in 1
print(unique_conso("raneem")) # It results in 3


# B

"""
Time complexity is O(N) since N is the length of our input, which are looping through and lowering its
characters n times.
Space complexity is O(26) since 26 is the number of letters in the alphabet and these are the ones occupying
space in memory while we loop. Or we can say that space complexity is O(alphabet) with alphabet holding
the number of letters in the alphabet.

We assume that the number of letters in the alphabet is constant as well as the input is a single string.
"""


# 2.2

def count_squares(x_grid):
    if x_grid <= 0: # Base case
        return 0
    else:
        return x_grid * x_grid + count_squares(x_grid-1) # Recursive case

# Tests

print(count_squares(1)) # It is 1
print(count_squares(2)) # It is 5
print(count_squares(3)) # It is 14
print(count_squares(4)) # It is 30
print(count_squares(5)) # It is 55

