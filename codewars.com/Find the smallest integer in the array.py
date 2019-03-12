# DATE: 12/03/19
#  URL: https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/python
'''
Given an array of integers your solution should find the smallest integer.

For example:

    Given [34, 15, 88, 2] your solution will return 2
    Given [34, -345, -1, 100] your solution will return -345

You can assume, for the purpose of this kata, that the supplied array will not be empty.

'''
def find_smallest_int(arr):
    holder = float('inf')
    for i in range(len(arr)):
        if arr[i] < holder:
            holder = arr[i]
    return holder
