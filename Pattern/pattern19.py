def pattern19():
    N = int(input("Enter the value of N: "))
    iniS = 0
    for i in range(N):
        print("*" * (N - i), end="")
        print(" " * iniS, end="")
        print("*" * (N - i))

        iniS += 2

    iniS = 2 * N - 2
    for i in range(1, N + 1):
        print("*" * i, end="")
        print(" " * iniS, end="")
        print("*" * i)
        iniS -= 2


pattern19()
