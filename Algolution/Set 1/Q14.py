def alternate_num():
    rows, cols = 5, 5
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if i % 2 == 1:
                print(j, end="")
            else:
                print(cols - j + 1, end="")
        print()

alternate_num()
