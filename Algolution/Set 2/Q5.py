'''Given an array arr[] of size n, return an equilibrium index (if any) or -1 if no equilibrium index
exists. The equilibrium index of an array is an index such that the sum of elements at lower
indexes equals the sum of elements at higher indexes.
Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.
Examples:

Input: arr[] = {-7, 1, 5, 2, -4, 3, 0}
Output: 4
Explanation: In 1-based indexing, 4 is an equilibrium index, because:

arr[1] + arr[2] + arr[3] = arr[5] + arr[6] + arr[7]

Input: arr[] = {1, 2, 3}
Output: -1
Explanation: There is no equilibrium index in the array.
Input:arr = {1, 3, 5, 2, 2}
Expected Output:2
Explanation: At index 2, the sum of elements on the left (1 + 3 = 4) is equal to the sum of
elements on the right (2 + 2 = 4).'''

def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        if left_sum == (total_sum - left_sum - num):
            return i + 1  # 1-based index
        left_sum += num
    return -1

# Example usage
arr = [-7, 1, 5, 2, -4, 3, 0]
print(find_equilibrium_index(arr))  # Output: 4
