#Source: https://stackoverflow.com/questions/71272910/attributeerror-spacy-tokenizer-tokenizer-object-has-no-attribute-tokens-from
import spacy
import re

regexp = re.compile('(?u)\\b\\w\\w+\\b')
en_nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
old_tokenizer = en_nlp.tokenizer

en_nlp.tokenizer = lambda string: old_tokenizer.tokens_from_list(
    regexp.findall(string))

def custom_tokenizer(document):
    doc_spacy = en_nlp(document)
    return [token.lemma_ for token in doc_spacy]

lemma_vect = CountVectorizer(tokenizer=custom_tokenizer, min_df=5)