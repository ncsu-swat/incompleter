import re

def substitutor():
    sentence1 = 'It is raining outside.'
    print(re.sub('raining', 'sunny', sentence1))
    print(re.sub('very', 'so', sentence2))
substitutor()