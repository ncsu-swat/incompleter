from math import factorial

def print_permutations_lexicographic_order(s):
    """Print all permutations of string s in lexicographic order."""
    seq = list(s)
    for _ in range(factorial(len(seq))):
        print(''.join(seq))
        nxt = get_next_permutation(seq)
        if nxt is None:
            seq.reverse()
        else:
            seq = nxt

def get_next_permutation(seq):
    """Return next greater lexicographic permutation. Return None if cannot.
 
    This will return the next greater permutation of seq in lexicographic
    order. If seq is the highest permutation then this will return None.
 
    seq is a list.
    """
    if len(seq) == 0:
        return None
    nxt = get_next_permutation(seq[1:])
    if nxt is None:
        seq[1:] = reversed(seq[1:])
        q = 1
        while q < len(seq) and seq[0] > seq[q]:
            q += 1
        if q == len(seq):
            return None
        (seq[0], seq[q]) = (seq[q], seq[0])
        return seq
    else:
        return [seq[0]] + nxt
print_permutations_lexicographic_order(s)