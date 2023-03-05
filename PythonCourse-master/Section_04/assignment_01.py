# Assignment 1

"""

Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.

twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True

"""
mylist = [0, 1, 2, 3, 4]
# mylist[0], mylist[4] = mylist[4], mylist[0]
# print(mylist)
# mylist[1], mylist[3] = mylist[3], mylist[1]
# print(mylist)

print(mylist.reverse())

#Your Code Below:



def twelver(a, b):
    return a == 12 or b == 12 or a+b == 12

result = twelver(0,8)

print(result)







# Solution:
# def twelver(a, b):
#   return (a == 12 or b == 12 or a+b == 12)
