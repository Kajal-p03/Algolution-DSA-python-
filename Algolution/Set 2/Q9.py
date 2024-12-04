'''Given an integer array, find the maximum length subarray having a given sum.(USE
HASHMAP Concept)
Input:nums[] = { 5, 6, -5, 5, 3, 5, 3, -2, 0 }target = 8
Output:{ -5, 5, 3, 5 }
Subarrays with sum 8 are { -5, 5, 3, 5 },{ 3, 5 },{ 5, 3 }
The longest subarray is { -5, 5, 3, 5 } having length 4.'''

def max_length_subarray(nums, target):
    prefix_sum = {}
    current_sum = 0
    max_length = 0
    start_index = -1

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum == target:
            max_length = i + 1

        if current_sum - target in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - target])

        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i

    return max_length

# Example usage
nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 8
print(max_length_subarray(nums, target))  # Output: 4
