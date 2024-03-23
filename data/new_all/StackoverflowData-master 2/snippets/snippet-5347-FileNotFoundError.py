#Source: https://stackoverflow.com/questions/63013036/filenotfounderror-errno-2-no-such-file-or-directory-apempe-chunks-txt
import os
import codecs
import string, re
from pathlib import Path


path = "C:\\Users\\Desktop\\texts\\dataset"
text_files = os.listdir(path)

documents = [open(f, encoding="utf-8").read() for f in text_files]
sparse_matrix = tfidf_vectorizer.fit_transform(documents)