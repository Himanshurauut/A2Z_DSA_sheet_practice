def pattern15():
    """
    pattern 15 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for row in range(1, N + 1):
        for character in range(0, N-row+1):
            print(chr(character + 65), end=" ")
        print()


pattern15()
