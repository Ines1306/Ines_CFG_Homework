"""
A
"""

from collections import deque

line_order = deque([])

with open("hw3_q1.txt", "r") as file:
    for line in file:
        line = line.strip() # this way we take the paragraphs (\n) of each line
        if line.startswith('JUMP'):
            name_jump = line.split()[1] # to get the second word (name) of each line
            line_order.appendleft(name_jump)
        else:
            name_join = line.split()[1]
            line_order.append(name_join)

print(list(line_order)) # This way we get a list with the correct order of who jumped and who joined


"""
B
"""

"""
The time complexity is O(n) as we are looping through n lines and performing strip, split and append functions
also n times. So it is linear as the time complexity depends on the number of lines.

The space complexity is also O(n) as we are adding n names into the list line_order. So everytime we are 
looping through a line, we add the respective name to the list n times.

As for assumptions we assume that each line has the same length, in this case two words, with the first
being JUMP/JOIN and the second one being a name.
If we were to have lines with more length the operations split and strip would take longer.

"""