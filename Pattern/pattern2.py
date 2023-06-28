def pattern2():
    """
    print the pattern 2 of gfg code
    :return:
    """
    N = int(input("Enter the value of N: "))
    for rows in range(1, N + 1):
        for columns in range(1, rows + 1):
            print("*", end=" ")
        print()


pattern2()
