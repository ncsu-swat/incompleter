def is_power_of_two(n):
    """Return True if n is a power of two."""
    if n <= 0:
        return False
    else:
        return n & n - 1 == 0
if is_power_of_two(n):
    print('{} is a power of two.'.format(n))
else:
    print('{} is not a power of two.'.format(n))