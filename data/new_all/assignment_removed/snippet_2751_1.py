def clear_rightmost_set_bit(n):
    """Clear rightmost set bit of n and return it."""
    return n & n - 1
n = int(input('Enter a number: '))
print('n with its rightmost set bit cleared equals:', ans)