from math import factorial

def print_permutations_lexicographic_order(s):
    """Print all permutations of string s in lexicographic order."""
    seq = list(s)
    for _ in range(factorial(len(seq))):
        print(''.join(seq))
        p = len(seq) - 1
        while p > 0 and seq[p - 1] > seq[p]:
            p -= 1
        seq[p:] = reversed(seq[p:])
        if p > 0:
            q = p
            while seq[p - 1] > seq[q]:
                q += 1
            (seq[p - 1], seq[q]) = (seq[q], seq[p - 1])
print_permutations_lexicographic_order(s)