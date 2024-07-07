def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j < i:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()

# Example usage:
n = 5
upper_triangular(n)
