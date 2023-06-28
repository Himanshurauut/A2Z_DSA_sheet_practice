def pattern10():
    """
    pattern 10 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for rows in range(1, 2 * N):
        stars = rows
        if rows > N:
            stars = 2 * N - rows
        for star in range(1, stars + 1):
            print("*", end=" ")
        print()


def alternative_pattern10():
    """
    pattern 10 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for rows in range(1, 2 * N):
        K = 0
        stars = rows
        if rows > N:
            stars = 2 * N - rows
        while K != stars:
            print("*", end=" ")
            K += 1
        K = 0
        print()


alternative_pattern10()
