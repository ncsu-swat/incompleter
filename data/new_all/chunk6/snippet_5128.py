#Source: https://stackoverflow.com/questions/46914866/why-will-i-get-a-typeerror-object-of-type-nonetype-has-no-len
words = [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes',"don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under']

def requirement(word):
    onelist = []
    if word in words:
        return(len(onelist.append(word)))


print(map(requirement('look'), words))