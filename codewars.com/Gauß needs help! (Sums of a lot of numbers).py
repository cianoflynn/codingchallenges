'''

Title: Gauß needs help! (Sums of a lot of numbers). 
url: https://www.codewars.com/kata/54df2067ecaa226eca000229
Date: 05.03.19
'''
def f(n):
    if type(n) != int or n <= 0.0:
        return None
    else:
        n = float(n)
        return (n/2)*(1+n)
 
