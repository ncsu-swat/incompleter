def vowel_count(str):
    vowel = set('aeiouAEIOU')
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
    print('No. of vowels :', count)
str = 'GeeksforGeeks'
vowel_count(str)