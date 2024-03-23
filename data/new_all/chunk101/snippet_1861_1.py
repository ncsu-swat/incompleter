import re

def substitutor():
    print(re.sub('raining', 'sunny', sentence1))
    sentence2 = 'Thank you very very much.'
    print(re.sub('very', 'so', sentence2))
substitutor()