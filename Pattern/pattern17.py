def pattern16():
    """
    pattern 16 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for row in range(N):

        for space in range(N - row - 1):
            print(end="#")

        ch = "A"
        breakpoints = (2 * row + 1) // 2

        for character in range(1, 2 * row + 2):
            print(ch, end="")
            if character <= breakpoints:
                ch = chr(ord(ch) + 1)
            else:
                ch = chr(ord(ch) - 1)
        for j in range(N - row - 1):
            print(end="#")
        print()


pattern16()
