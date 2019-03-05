'''
date: 27/02/19
description: accum("abcd") -> "A-Bb-Ccc-Dddd"
url: https://www.codewars.com/kata/mumbling/python
'''
def accum(s):
    outlist = ''
    for i in range(0,len(s)+1):
        list = s[i-1]*i
        list2 = list.capitalize()
        outlist = outlist+'-'+list2
    return (outlist[2:])
