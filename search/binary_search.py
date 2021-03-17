'''
This assignment is a part of the course "Data Structures and Algorithms in Python". (https://jovian.ai)
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.
Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
'''
from evaluate_tests import evaluate_tests

tests = [
    {'input': {'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, 'output': 3},
    {'input': {'nums': [13, 23, 25, 29, 34, 1, 7, 8]}, 'output': 5},
    {'input': {'nums': [1, 4, 8, 9, 12]}, 'output': 0},
    {'input': {'nums': [55, 1, 4, 8, 9, 12]}, 'output': 1},
    {'input': {'nums': [13, 23, 25, 29, 34, 1]}, 'output': 5},
    {'input': {'nums': [0, 5, 7, 8, 11, 12]}, 'output': 0},
    {'input': {'nums': []}, 'output': 0},
    {'input': {'nums': [67]}, 'output': 0},
    {'input': {'nums': [34, 1]}, 'output': 1}
    ]


def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)-1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        # Uncomment the next line for logging the values and fixing errors.
        # print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid number:", nums[mid])
        
        if mid > 0 and nums[mid-1] > nums[mid]:
            # The middle position is the answer
            return mid
        
        elif nums[mid] < nums[-1]:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return 0

evaluate_tests(count_rotations_binary, tests)