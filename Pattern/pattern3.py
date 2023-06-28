def pattern3():
    """
    print the pattern 3 of gfg
    :return: null
    """
    N = int(input("Enter the N value: "))
    for rows in range(1, N + 1):
        for columns in range(1, rows + 1):
            print(columns, end=" ")
        print()


pattern3()
