def pattern13():
    """
    pattern 13 solution in gfg
    :return:
    """
    N = int(input("Enter the value of N: "))
    count = 1
    for row in range(1, N + 1):
        for _ in range(1,row+1):
            print(count,end=" ")
            count +=1
        print()


pattern13()