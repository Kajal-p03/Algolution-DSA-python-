#WAP to merge two sorted array to a third array 

a1 = [3,6,9,12,15]
a2 = [2,5,8,10,13]
a3 = []

p1 = 0 
p2 = 0

while(p1<len(a1) and p2<len(a2)):
    if a1[p1] <=a2[p2]:
        a3.append(a1[p1])
        p1 +=1
    else:
        a3.append(a2[p2])
        p2 += 1

if p1 == len(a1):
    while(p2 < len(a2)):
        a3.append(a2[p2])
        p2 += 1
elif p2 == len(a2):
    while(p1 <len(a1)):
        a3.append(a1[p1])
        p1 += 1
        p1 +=1

print(a3)                         