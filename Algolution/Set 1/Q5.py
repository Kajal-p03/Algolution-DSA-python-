# program that takes 5 integer as input and finds order of number in array is palindrome 
numbers = []
print("enter 5 integer:")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

if numbers == numbers[::-1]:
    print("numbers forms palndrome")
else :
    print("number does not forms palindrome")       