# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

# Your Code Below
"""def sequence(numbers):
    for num in list(range(len(numbers))):
        print(numbers)
        if numbers == range(4):
            print(numbers)
            return True
        print(numbers)
    return False
sequence([1, 1, 2, 3, 1]) → True

print(sequence([1,2,3]))"""

def find_sequence(lst):
    for i in range(len(lst)-1):
        if lst[i:i+3] == [1, 2, 3]:
            return True
    return False
result = find_sequence([5,3,3,1,2,3])
print(result)


# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False
