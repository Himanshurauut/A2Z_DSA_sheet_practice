def pattern5():
    """
    pattern 5 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for rows in range(1, N + 1):
        for columns in range(1, N - rows + 2):
            print("*", end=" ")
        print()


def pattern5_1():
    """
    alternative solution pattern 5 in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for i in range(N, 0, -1):
        print('* ' * i)


pattern5()
