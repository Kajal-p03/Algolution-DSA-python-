'''
*
**
***
****
*****
****
***
**
*'''
def print_half_diamond(columns):
    for i in range(1, columns + 1):
        print('*' * i)

    for i in range(columns - 1, 0, -1):
        print('*' * i)

num_columns = int(input("Enter the number of columns: "))
print_half_diamond(num_columns)