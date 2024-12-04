# search a number in array
numbers = []
n = int(input("enter number of elements:"))
print("Enter the numbers:")
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

search_num = int(input("enter the number to search for:"))    

if search_num in numbers:
    index = numbers.index(search_num)
    print(f"number {search_num} is found at index {index}.")
else:
    print("-1")   