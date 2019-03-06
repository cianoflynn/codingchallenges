# Date: 06/03/19
# URL: https://www.codewars.com/kata/compare-strings-by-sum-of-chars/python
#
'''
Compare two strings by comparing the sum of their values (ASCII character code).

    For comparing treat all letters as UpperCase
    null/NULL/Nil/None should be treated as empty strings
    If the string contains other characters than letters, treat the whole string as it would be empty

Your method should return true, if the strings are equal and false if they are not equal.
Examples:

"AD", "BC"  -> equal
"AD", "DD"  -> not equal
"gf", "FG"  -> equal
"zz1", ""   -> equal (both are considered empty)
"ZzZz", "ffPFF" -> equal
"kl", "lz"  -> not equal
null, ""    -> equal
'''




def compare(s1,s2):
    if s1 == None:
        s1 = ''
    if s1.isalpha() == False: 
        s1 = ''
    if s2 == None:
        s2 = ''
    if s2.isalpha() == False:
        s2 = ''
    a = sum(map(ord,s1.upper()))
    b = sum(map(ord,s2.upper()))
    return (a == b)
