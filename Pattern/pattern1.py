def pattern1():
    """
    print the pattern1 in gfg 
    :return:
    """
    N = int(input("Enter the value of N: "))
    for rows in range(1, N + 1):
        for columns in range(1, N + 1):
            print("*", end=" ")
        print()


pattern1()
