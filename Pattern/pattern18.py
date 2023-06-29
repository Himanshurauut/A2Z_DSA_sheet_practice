def pattern18():
    """
    pattern 17 own solution not accurate
    :return:
    """
    N = int(input("Enter the value of N: "))
    for row in range(N):

        ch = 'A'
        for character in range(0, row + 1):
            print(chr(ord(ch) + N - row - 1), end="")
            ch = chr(ord(ch) + 1)
        print()


def alternative_perfect_solution():
    """
    pattern 17 own solution not accurate
    :return:
    """
    N = int(input("Enter the value of N: "))
    for row in range(N):

        for character in range(0, row + 1):
            print(chr(65 + N - character - 1), end="")
        print()


pattern18()
