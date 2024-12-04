'''12345
23455
34555
45555
55555'''
def question16():
    rows = 5
    for i in range(1, rows + 1):
        # First loop to print numbers from i to rows
        for j in range(i, rows + 1):
            print(j, end="")
        
        # Second loop to print 'rows' for the remaining positions
        for j in range(2, i + 1):
            print(rows, end="")
        
        # Move to the next line after each row
        print()

# Example usage
question16()
