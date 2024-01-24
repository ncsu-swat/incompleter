#Source: https://stackoverflow.com/questions/53765719/filenotfounderror-in-python-during-arabic-text-analysis
from sklearn.feature_extraction.text import TfidfVectorizer

import os

text_files= os.listdir(r"C:\Users\Nujou\Desktop\Master\thesis\corpora\modified Corpora\Training set\5K\ST")

documents= []
for f in text_files:
    file= open(f, 'r', 'utf-8-sig')
    documents.append(file.read())
tfidf = TfidfVectorizer().fit_transform(documents)
# no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = tfidf * tfidf.T