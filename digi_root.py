# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 08:46:31 2019

@author: creddersen
"""

    """
    A digital root is the recursive sum of all the digits in a number.
    Given n, take the sum of the digits of n. 
    If that value has more than one digit, continue reducing in this
    way until a single-digit number is produced. 
    This is only applicable to the natural numbers.
    """
def digital_root(n = None):
    #This block of code returns the sum of all the numbers in n. 
    #It also counts the digits in n. 
    #If no argument, the function returns 0
    if n:

        numbers = [int(x) for x in str(n)]
        Sum = sum(numbers)
        total = 0
        for num in numbers:
            total += 1
    
      #This block is what makes the function recursive, until a single digit is
      #produced
        if total > 1: 
            while total > 1:
                new_number = Sum
                new_numbers_list = [int(y) for y in str(new_number)] 
                new_Sum = sum(new_numbers_list)
                total -= 1
            return new_Sum
    else:
        return 0
    
