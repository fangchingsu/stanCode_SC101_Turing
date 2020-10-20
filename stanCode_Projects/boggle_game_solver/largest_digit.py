"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))  # 5
    print(find_largest_digit(281))  # 8
    print(find_largest_digit(6))  # 6
    print(find_largest_digit(-111))  # 1
    print(find_largest_digit(-9453))  # 9


def find_largest_digit(n):
    """
    :param n:
    :return:
    """
    l_dig = 0
    return find_largest_digit_helper(n, l_dig)


def find_largest_digit_helper(n, l_dig):
    if n < 0:
        n = -n
    if n != 0:
        mod_n = n % 10
        if mod_n > l_dig:
            l_dig = mod_n
        return find_largest_digit_helper(n // 10, l_dig)
    else:
        return l_dig


if __name__ == '__main__':
    main()
