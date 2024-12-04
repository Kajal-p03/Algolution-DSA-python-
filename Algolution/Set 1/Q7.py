#print all unique numbers in an array 
numbers = []
n = int(input("enter numbers of elements in the array"))

print("enter the numbers")
for i in range(n):
    num = int(input(f"enter number {i+1}:"))
    numbers.append(num)

unique_numbers = []

for num in numbers:
    if numbers.count(num) ==1:
        unique_numbers.append(num)

if unique_numbers:
    print("the unique numbers in the array are :", unique_numbers)
else:
    print("there are no unique numbers in the array")