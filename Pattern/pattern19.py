def pattern19(N):
    for row in range(2 * N):
        for star in range(0, N - row):
            print("*", end="")
        for space in range(0, 2 * row):
            print(" ", end="")
        for star in range(0, N - row):
            print("*", end="")
        print()

    spaces = 2 * N - 2
    for row in range(0, N):
        for star in range(0, row + 1):
            print("*", end="")
        for space in range(0, spaces):
            print(" ", end="")
        for star in range(0, row + 1):
            print("*", end="")
        spaces -= 2
        print()

pattern19(3)


