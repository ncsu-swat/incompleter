def vowel_count(str):
    count = 0
    vowel = set('aeiouAEIOU')
    for alphabet in str:
        if alphabet in vowel:
    print('No. of vowels :', count)
str = 'GeeksforGeeks'
vowel_count(str)