def pattern11():
    """
    pattern 11 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for rows in range(0, N):
        if rows % 2 == 0:
            start = 1
        else:
            start = 0
        for no in range(0, rows + 1):
            print(start, end=" ")
            start = 1 - start
        print()


pattern11()
