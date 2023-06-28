def pattern4():
    """
    Alternative method to print the pattern using while loop and for loop
    :return: null
    """
    N = int(input("Enter the N value: "))
    for rows in range(1, N + 1):
        columns = 1
        while rows >= columns:
            print(rows, end=" ")
            columns += 1
        print()


pattern4()
