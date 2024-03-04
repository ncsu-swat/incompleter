#Source: https://stackoverflow.com/questions/67212594/attributeerror-pathdistribution-object-has-no-attribute-name
import os
import json
import spacy
import logging
from datetime import datetime, timedelta

from celeryapp import app

sp = spacy.load('en_core_web_sm')

@app.task(bind=True)
def extract(self, filename):
    file_path = os.path.join(os.getcwd(), 'data', filename)
    doc = open(file_path).read()
    print('Extract called')
    return doc

@app.task(bind=True)
def transform_tokenize_doc(self, doc:str):
    sentences = []

    for sent in sp(doc).sents:
        sentences.append(str(sent).strip())

    return sentences

@app.task(bind=True)
def load(self, filename, *args):
    with open(os.path.join(os.getcwd(), 'output', filename), 'a+') as file:
        file.write(json.dumps(args, indent=4))


if __name__ == '__main__':
    tasks = []

    for filename in os.listdir(os.path.join(os.getcwd(), 'data'))[:10]:
        print(f'filename is {filename}')
        etl = (extract.s(filename) | transform_tokenize_doc.s() | load.s(filename)).apply_async()
        tasks.append(etl)

    for task in tasks:
        task.get()