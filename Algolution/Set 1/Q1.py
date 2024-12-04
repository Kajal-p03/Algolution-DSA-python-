# count total number of negative numbers in an array 

def count_negative_numbers(arr):
    count = 0

    for i in arr:
        if i < 0 :
            count += 1

    return count 
array = [-1,-2,-3,1,2,3]
print("Total number of negative values are" , count_negative_numbers(array))       
