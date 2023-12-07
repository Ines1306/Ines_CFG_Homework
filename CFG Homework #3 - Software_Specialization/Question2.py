"""
A

8, 15, 22, 29, 36, …
For example:
● num_in_seq(1) = 8
● num_in_seq(5) = 36
● num_in_seq(10) = 71
"""

def num_in_seq(number):
    if number <= 0: # Base case for number <= 0
        return 0
    elif number == 1: # Base case for number = 1
        return 8
    else: # Recursive case
        return 7 + num_in_seq(number-1)

print(num_in_seq(-1)) # 0
print(num_in_seq(0)) # 0
print(num_in_seq(1)) # 8
print(num_in_seq(2)) # 15
print(num_in_seq(3)) # 22
print(num_in_seq(4)) # 29
print(num_in_seq(5)) # 36
print(num_in_seq(10)) # 71