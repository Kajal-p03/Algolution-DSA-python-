'''Given an integer array arr[] of size n, the task is to find the count inversions of the given array.
Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.
Input: arr[] = {7, 2, 6, 3}
Output: 4
Explanation: Given array has 4 inversions: (7, 2), (7, 6), (7, 3), (6, 3)'''

def count_inversions(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

arr = [7, 2, 6, 3]
print(count_inversions(arr)) 
