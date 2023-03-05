# Assignment 1:
"""
Print Bill's salary from the my_list object shown below.

my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

"""


# your code below:


my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

new_list = (my_list[1].insert(2, 'phone'))
print(new_list)
print(my_list[0].get("Bill"))































# Solution
# print(my_list[0].get('Bill'))
