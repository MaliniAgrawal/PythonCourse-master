
# Assignment 5

"""
Define a method that accepts a list as an argument
and returns True if one of the first_folder 4 elements
in the list is a 6. The list length may be less than 4.


first3([1, 2, 6, 3, 4]) → True
first3([1, 2, 3, 4, 6]) → False
first3([1, 2, 3, 4, 5]) → False

"""

# Your Code Below:
def first3(numbers):
    # First figure the end for the loop
    end = len(numbers)
    if end > 4:
        end = 4

    for i in range(end):  # loop over index [0, 1, 2, 3]
        if numbers[i] == 6:
            return True
    return False

print(first3([1,2,5,3,5,6,6]))





















# Solution:

# def first3(numbers):
#     # First figure the end for the loop
#     end = len(numbers)
#     if end > 4:
#         end = 4
#
#     for i in range(end):  # loop over index [0, 1, 2, 3]
#         if numbers[i] == 6:
#             return True
#     return False
