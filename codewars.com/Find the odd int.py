# DATE:  11/03/19
#  URL: https://www.codewars.com/kata/find-the-odd-int/train/python
'''
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
'''


def find_it(seq):
    list = [i for i in seq if seq.count(i)%2!=0][0]
    return list[0]
