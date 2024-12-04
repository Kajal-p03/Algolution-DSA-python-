#WAP that takes 5 integers as input from the user and print max of all the numbers 

l = []
i = 0 

while(i<5):
    a = int(input("enter values:-"))
    l.append(a)
    i += 1

max = l[0]
for i in range(1,5):
    if l[i]>max:
        max=l[i]
print("max value out of five values is",max)        