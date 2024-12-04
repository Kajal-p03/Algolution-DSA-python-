# count total number of duplicate numbers in an array  
numbers = []
n = int(input("Enter the number of elements in the array: "))

print("Enter the numbers:")
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

frequency = {}
duplicate_count = 0

for num in numbers:
    if num in frequency:
        if frequency[num] ==1:
            duplicate_count +=1
        frequency[num] += 1
    else:
        frequency[num] = 1

print(f"total numbers of duplicate numbers in the array:{duplicate_count}")  