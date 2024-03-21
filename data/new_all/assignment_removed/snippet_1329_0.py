def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))