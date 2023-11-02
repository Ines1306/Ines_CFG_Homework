# Section 3

import math

def allocation(number_students):
    # First let's create an empty dictionary
    distribution_classes= {}
    # The maximum number of students per class is 30
    max_students_class = 30
    # There should be at least 2 classes but the minimum number of classes as well
    min_number_classes = 2

    # Let's check the number of classes needed
    number_classes = max(min_number_classes, math.ceil(number_students/max_students_class))
    # Now, let's calculate the number of students per class
    students_per_class = int(number_students/number_classes) # to get a whole number
    students_left = number_students % number_classes

    # Distributing students per class evenly
    for number in range(number_classes):
        # Let's check if there are students left after dividing them per class
        if students_left > 0:
            # Assigning keys and values to the dictionary
            distribution_classes[f"Class {number + 1}"] = students_per_class + 1
            students_left = students_left - 1
        else:
            distribution_classes[f"Class {number + 1}"] = students_per_class

    print(f"Proposed allocation: {number_classes} classes")
    print(f"{distribution_classes}")

# Testing
allocation(31)
allocation(59)
allocation(87)