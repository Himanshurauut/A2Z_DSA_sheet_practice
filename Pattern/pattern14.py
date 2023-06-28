def pattern14():
    """
    pattern 14 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for row in range(1, N + 1):
        for character in range(0, row):
            print(chr(character + 65), end=" ")
        print()


pattern14()
