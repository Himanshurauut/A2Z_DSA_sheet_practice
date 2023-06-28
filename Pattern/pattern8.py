def pattern8():
    """
    pattern 8 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for rows in range(1, N + 1):
        for space in range(1, rows):
            print(" ", end="")
        for stars in range(1, (N - rows) * 2 + 2):
            print("*", end="")
        for space in range(1, rows):
            print(" ", end="")
        print()


def alternative_pattern():
    """
    alternative solution for pattern 8
    :return:
    """
    N = int(input("Enter the value of N: "))
    k = 0
    for rows in range(0, N):
        for space in range(0, rows + 1):
            print(end=" ")
        while k != (N - rows) * 2 - 1:
            print("*", end="")
            k += 1
        k = 0
        print()


pattern8()
