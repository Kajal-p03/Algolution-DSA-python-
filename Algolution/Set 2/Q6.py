'''Given a sorted array A (sorted in ascending order), having N integers, find if there exists any
pair of elements (A[i], A[j]) such that their sum is equal to X.
a)Using Naive Approach
b)Using Two Pointer Technique
Input: A = [1, 2, 4, 5, 7, 11]
N = 6
X = 9
Expected Output: Yes
(Explanation: The pair (2, 7) sums to 9.)'''

# NAIVE APPROACH
def has_pair_naive(arr, x):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == x:
                return True
    return False

# Example usage
arr = [1, 2, 4, 5, 7, 11]
x = 9
print(has_pair_naive(arr, x))  # Output: True


#Two pointer approach
def has_pair_two_pointer(arr, x):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == x:
            return True
        elif current_sum < x:
            left += 1
        else:
            right -= 1
    return False

# Example usage
arr = [1, 2, 4, 5, 7, 11]
x = 9
print(has_pair_two_pointer(arr, x))  # Output: True
