"""Provide utility functions for text preprocessing"""
import classifier
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import porter

def _clean_ipc_list(list_ipc):
    list_ipc_clean = [element['ic'] for element in list_ipc if not isinstance(element, str)]
    return list_ipc_clean

def _extract_fields(text_patent):
    soup = BeautifulSoup(text_patent, "lxml")
    tag_record = soup.record
    number = tag_record['pn']
    tag_ipcs = soup.ipcs
    ipcs = tag_ipcs['mc']
    list_ipc = _clean_ipc_list(tag_ipcs.contents)
    tag_abstract = soup.ab
    abstract = tag_abstract.text
    return classifier.models.PatentDocument(number, ipcs, list_ipc, abstract)

def _extract_word_list(text):
    list_words = text.split()
    english_stopwords = set(stopwords.words('english'))
    list_without_stopwords = [word for word in list_words if word not in english_stopwords]
    set_unique_words = set(list_without_stopwords)
    return set_unique_words

def stem_words_list(list_words):
    """Stem words using a nltk stemmer

    :param list_words: A list of strings representing words to stem
    :rtype: A list of strings representing stemmed words
    """
    stemmer_porter = porter.PorterStemmer()
    list_words_stemmed = [stemmer_porter.stem(word) for word in list_words]
    return list_words_stemmed
