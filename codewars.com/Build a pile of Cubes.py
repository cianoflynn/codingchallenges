# DATE: 19/03/2019
#  URL: https://www.codewars.com/kata/build-a-pile-of-cubes/python 
'''
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.
Examples:

findNb(1071225) --> 45
findNb(91716553919377) --> -1

mov rdi, 1071225
call find_nb            ; rax <-- 45

mov rdi, 91716553919377
call find_nb            ; rax <-- -1
'''
def find_nb(m):
    if m == 1:
        return 1
    else:
        n, vol = [2, 1]
        while vol <= m:
            vol += n**3
            if vol == m:
                return n
            else:
                n += 1
                continue
        return -1
