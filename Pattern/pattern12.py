def pattern12():
    """
    pattern 12 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for row in range(1, N + 1):
        k = row
        for n in range(1, row + 1):
            print(n, end="")
        for space in range(1, (2 * (N - row)) + 1):
            print(end=" ")
        while k != 0:
            print(k, end="")
            k -= 1
        print()


pattern12()
