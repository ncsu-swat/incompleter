def chars_mix_up(a, b):
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))