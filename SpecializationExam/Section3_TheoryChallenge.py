# 3.1

"""
Let's think of an input with my name using the ASCII code, so ines. Let's do the hashing (process to match
data to an integer value).

So ASCII values are:
'i' = 105
'n' = 110
'e' = 101
's' = 115

The sum is 431.
Let's think of a hash table - the location where the values are going to be stored in a list - of 15.
The size of the hash table is small since we are expecting few elements and this way we reduce the hash
collisions as well as reduce memory constraints.

The hash value is 431 % 15 = 1
"""


# 3.2

"""
So we already have the input "ines" in the hash table. Let's use the example of my brother's name: joao.

So ASCII values are:
'j' = 106
'o' = 111
'a' = 97
'o' = 111

The sum is 425.
The hash value is 425 % 15 = 10.
In this case there is no hash collision since 'ines' will be stored in 1 and 'joao' will be stored in '10'
in the hash table, therefore these are different indexes.
"""

# 3.3

"""
For a hash collision let's think of an input that results in hash value 1.
Since my brother loves apples, let's do apple:

'a' = 97
'p' = 12
'p' = 112
'l' = 108
'e' = 101


The sum is 530.
The hash value is 530 % 15 = 1

In this case there will be a hash collision which can be resolved with:
1. Chaining: make each array slot hold a pointer to a linked list that has the values of all keys in that index
2. Open-addressing: if the initial index already has a value, the next slot is checked until an empty one is found

So if we were to use chaining the index would have a linked list of the key-value pairs.
So what's inside 1 will become a pointer that will point to a node with key = 'ines' and its value.
This node will point to the next one which contains 'apple' and its value. The hash collision is handled!
"""