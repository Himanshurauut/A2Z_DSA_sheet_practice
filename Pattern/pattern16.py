def pattern16():
    """
    pattern 16 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    for row in range(0, N):
        for space in range(0, N - row - 1):
            print(end="#")
        for character in range(0, (2 * row) +1):
            print(chr(character + 65), end="")
            if character <= (2*row+1)//2:
                character += 1
            else:
                character -= 1
        print()


pattern16()
