# DATE: 13/03/2019
#  URL: https://www.codewars.com/kata/exes-and-ohs/train/python  
'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''
#  s = s.lower()
#    return s.count('x') == s.count('o')
#   return s.lower().count('x') == s.lower().count('o')
def xo(s):
    xcount = 0
    ocount = 0
    l = list(s.lower())
    for i in l:
        if i == 'x':
            xcount +=1
        if i == 'o':
            ocount +=1
    return xcount == ocount

