def pattern7():
    """
    pattern 7 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for rows in range(1, N + 1):
        for space in range(1, N - rows + 1):
            print(" ", end="")
        for stars in range(0, 2 * rows - 1):
            print("*", end="")
        for space in range(1, N - rows + 1):
            print(" ", end="")
        print()


def alternative_pattern():
    """
    alternative solution for pattern 7
    :return:
    """
    N = int(input("Enter the value of N: "))
    k = 0
    for rows in range(1, N + 1):
        for space in range(1, (N - rows) + 1):
            print(end=" ")
        while k != (2 * rows) - 1:
            print("*", end="")
            k += 1
        k = 0
        print()


alternative_pattern()
