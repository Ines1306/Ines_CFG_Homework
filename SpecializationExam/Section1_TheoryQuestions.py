"""
1.1 The deque module is part of which python library?
1 point
"""

"""
It is part of the collections library.
"""


"""
1.2 What are 2 differences that distinguish a tree from a graph? 
2 points
"""

"""
In a tree a unique node is identified as the root. In a graph there isn't a unique node identified as a root.
Trees are not able to form circles. Graphs are able to form circles.
"""


"""
1.3 Give the definitions of time complexity and space complexity 
2 points
"""

"""
Time complexity measures the amount of time an algorithm takes to run (its running time).
Space complexity measures the amount of memory used by an algorithm needed to run, 
in terms of the size of the input.
"""


"""
1.4 Describe the bubble sort algorithm and its complexity. What is guaranteed at the end of the first
pass? 
5 points 
"""

"""
Bubble sort compares each pair of adjacent elements and swaps them repeatedly in case these are 
in the wrong order until the list is sorted. 
In the worst case scenario the time complexity is of O(n^2) because there are n*n comparisons.
In the best case scenario the time complexity is of O(n) in case the array is already sorted so only
n comparisons are performed.
The space complexity is of O(1) since we change the input directly.

At the end of the first pass it is guaranteed that the largest element is at the end of the array
since it will be moved all the way to the end due to being the maximum value of the array.
"""


"""
1.5 Explain what LIFO and FIFO are and how each works in practice with a named data structure
8 points
"""

"""
LIFO means last-in first-out.
FIFO means first-in first-out.

Stacks are collections of objects that act according to the LIFO principle.
As a practical example if we have a stack of books and we need to add a new one, we add a book 
to the top of the stack and if need to remove a book, we also remove the one from the top.

Queue are collections of objects that act according to the FIFO principle.
As a practical example if we have a queue of documents to print, the first document that we open and click
"print" is the first one to be printed and the first one to leave the queue as well, so it is the first
document to be added and the first to be removed.
"""


""" 
1.6 What is a Balanced Binary Tree and what would be the best root? 
Walkthrough how you search using this structure. 
8 points
"""

"""
A balanced binary tree is a binary tree where the right and left subtrees of any node 
differ in height by at most one. For each node, its left and its right subtrees are also balanced binary trees.
The best root would be the one that could maximize the balance of the tree, with the minimum height possible.
We would use the middle value as the root and then have the smaller values on the left of the tree and the
larger values on the right of the tree.

To search in a balanced binary tree we can use a top-down approach. For this we start at the root, if the value
we are looking for is bigger or smaller than the root value, we move left (smaller) or right (bigger).
We repeat this on the subtree and on the next one and so on until the value we want is found or we
realize that this value does not exist.
"""