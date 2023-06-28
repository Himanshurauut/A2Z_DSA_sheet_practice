def pattern6():
    """
    pattern 6 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for rows in range(1, N + 1):
        for columns in range(1, N - rows + 2):
            print(columns, end=" ")
        print()


pattern6()
