'''11111
10001
10001
10001
11111'''

def question15():
    rows, cols = 5, 5
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if i == 1 or i == rows or j == 1 or j == cols:
                print("1", end="")
            else:
                print("0", end="")
        print()
question15()
