# DATE: 13/03/19
#  URL: https://www.codewars.com/kata/shortest-word
'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

'''
# Other approached ->  return min(len(x) for x in s.split()) -> return len(min(s.split(' '), key=len)) -> return min(map(len, s.split(' ')))
def find_short(s):
    li = sorted(list(s.split(" ")),  key=len)
    return len(li[0])
