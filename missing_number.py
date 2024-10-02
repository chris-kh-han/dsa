'''
Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the array and the number of elements that needs to be in array.  For example if we want to find missing number from 1 to 6 the second parameter will be 6.
'''

def missing_number(arr, n):
   for num in range(1, n):
       if num not in arr:
           return num


