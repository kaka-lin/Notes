import sys


def matrix_chain_product(l, n):
    """
    Matrix Chain Multiplication:

    given a list of integers corresponding to the dimensions
    of each pair of matrices forming a chain.

    Args:
        l: A list of integers corresponding to the dimensions.
        n: The length of l

    Returns:
        M: is the minimum number of scalar multiplications needed
          to compute the product of matrices A(i), A(i+1), ..., A(j)
        B: is the index of the matrix after which the product
          is split in an optimal parenthesization of the matrix product.
    """
    # Initialize: Build the table
    M = [[0] * n for _ in range(n)]
    B = [[0] * n for _ in range(n)]

    # Base case: 1~n 對角線上皆為 0
    for i in range(1, n):
        M[i][i] = 0

    # compute table
    for p in range(2, n): # p is the chain length (subsequence lengths)
        for i in range(1, n - p + 1): # all i, j combinations
            j = i + p - 1
            M[i][j] = sys.maxsize
            for k in range(i, j): # find the best k
                q = M[i][k] + M[k + 1][j] + l[i-1]*l[k]*l[j]
                if q < M[i][j]:
                    M[i][j] = q
                    B[i][j] = k

    return (M[1][n-1], B[1][n-1])


if __name__ == "__main__":
    dimensions_list = [30, 35, 15, 5, 10, 20, 25]
    n = len(dimensions_list)
    # (15125, 3)
    min_num, index = matrix_chain_product(dimensions_list, n)
    print(f'Minimum number of multiplications is: {min_num}, and index is {index}')
