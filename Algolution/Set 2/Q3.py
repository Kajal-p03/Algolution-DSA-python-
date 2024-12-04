'''Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Solve it without sorting.
Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5'''

import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(nums, k))  # Output: 5
