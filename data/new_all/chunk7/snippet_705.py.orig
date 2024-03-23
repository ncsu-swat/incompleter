#Source: https://stackoverflow.com/questions/53765719/filenotfounderror-in-python-during-arabic-text-analysis
from sklearn.feature_extraction.text import TfidfVectorizer

text_files= r"C:\Users\Nujou\Desktop\Master\thesis\corpora\modified Corpora\Training set\5K\ST"
for f in text_files:
    documents= open(f, 'r', encoding='utf-8-sig').read()
tfidf = TfidfVectorizer().fit_transform(documents)
# no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = tfidf * tfidf.T