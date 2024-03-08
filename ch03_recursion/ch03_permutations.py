"""
Permutations of given text
"""


def calc_permutations(text: str) -> str:
    """
    Calculate all permutations for given text

    Parameters
    ----------
    text: Input text

    Returns
    -------
    str: Comma separated all permutations of given text
    """
    for i in range(0, 6):
        for j in range(0, i + 1):
            if i == j or j == 0:
                print(1, end=" ")
            else:
                if i > 3 and (j == 2):
                   print(i + j, end=" ")
                else:
                    print(i, end=" ")
        print("\n")


def pascal(row, col):
    print(f"{row=}, {col=}")
    if (row == 1 and col == 1) or (row > 0 and col == 1) or (0 < row == col):
        return 1
    else:
        return pascal(row - 1, col) + pascal(row - 1, col - 1)


if __name__ == "__main__":
    calc_permutations("abc")
    # resp = pascal(6, 5)
    # print(resp)
