'''
Description:   There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

    Find the unique number (this kata)
    Find the unique string
    Find The Unique

Date: 04/03/19
'''

from collections import Counter
def find_uniq(arr):
    c = Counter(arr)
    return next((x for x in arr if c[x] == 1), -1)

def find_uniq2(arr):
    already = {}
    for i in arr:
        if i in already:
            already[i] += 1
        else:
            already[i] = 1

    for i in arr:
        if already[i] == 1:
            return i
