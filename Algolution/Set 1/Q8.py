#count frequency of each number in an array 

numbers = []
n = int(input("Enter the number of elements in the array: "))

print("Enter the numbers:")
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1 
    else:
        frequency[num] = 1   

print("The frequency of each number in the array is:")
for num, count in frequency.items():
    print(f"{num}: {count} times") 