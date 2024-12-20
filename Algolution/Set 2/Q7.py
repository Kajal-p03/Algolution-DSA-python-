'''Given an array of integers of size ‘n’, Our aim is to calculate the maximum sum of ‘k’
consecutive elements in the array(Using Sliding Window Technique)
Input : arr[] = {100, 200, 300, 400}, k = 2
Output : 700
Input : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.
Input : arr[] = {2, 3}, k = 3
Output : Invalid
There is no subarray of size 3 as size of whole array is 2.'''

def max_sum_k_consecutive(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid"
    max_sum = sum(arr[:k])
    window_sum = max_sum

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum_k_consecutive(arr, k))  # Output: 39
