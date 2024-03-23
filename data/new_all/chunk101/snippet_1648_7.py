def mirrorChars(input, k):
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original, reverse))
    suffix = input[k - 1:]
    mirror = ''
    for i in range(0, len(suffix)):
        mirror = mirror + dictChars[suffix[i]]
    print(prefix + mirror)
if __name__ == '__main__':
    input = 'paradox'
    k = 3
    mirrorChars(input, k)