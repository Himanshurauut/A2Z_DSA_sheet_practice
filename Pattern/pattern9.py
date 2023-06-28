def pattern9():
    """
    pattern 9 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    # upward Half triangle
    for rows in range(1, N + 1):
        for space in range(1, N - rows + 1):
            print(" ", end="")
        for stars in range(0, 2 * rows - 1):
            print("*", end="")
        for space in range(1, N - rows + 1):
            print(" ", end="")
        print()

    # downward half triangle
    for rows in range(1, N + 1):
        for space in range(1, rows):
            print(" ", end="")
        for stars in range(1, (N - rows) * 2 + 2):
            print("*", end="")
        for space in range(1, rows):
            print(" ", end="")
        print()

def alternative_pattern9():
    """
    pattern 9 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    # upward Half triangle
    k = 0
    for rows in range(1, N + 1):
        for space in range(1, (N - rows) + 1):
            print(end=" ")
        while k != (2 * rows) - 1:
            print("*", end="")
            k += 1
        k = 0
        print()

    # downward half triangle
    k = 0
    for rows in range(1, N + 1):
        for space in range(1, rows):
            print(end=" ")
        while k != (N - rows) * 2 + 1:
            print("*", end="")
            k += 1
        k = 0
        print()


alternative_pattern9()
