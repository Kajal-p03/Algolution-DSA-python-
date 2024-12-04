'''pattern printing 1 
    *****
   *****
  *****
 *****
*****'''
rows = 5  

for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * 5)