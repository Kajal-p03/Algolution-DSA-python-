# take 7 interger num and reverse in array 
numbers = []
print(input("Enter 7 integers: "))
for i in range(7):
    num = int(input(f"enter number{i+1}:"))
    numbers.append(num)

reversed_numbers = numbers[::-1]

print("the reversed order of number is:")
for num in reversed_numbers:
    print(num)