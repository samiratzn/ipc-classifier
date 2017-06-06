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

def _stem_words_list(list_words):
    """Stem words using a nltk stemmer

    :param list_words: A list of strings representing words to stem
    :rtype: A list of strings representing stemmed words
    """
    stemmer_porter = porter.PorterStemmer()
    list_words_stemmed = [stemmer_porter.stem(word) for word in list_words]
    return list_words_stemmed

def get_patent(text_patent):
    """Field extraction exposed wrapper

    :param text_patent: A string, is a patent file's text
    """
    return _extract_fields(text_patent)

def transform_patent(patent):
    """Process text inside its patent object container

    :param patent: A PatentDocument object
    """
    patent.abstract = _extract_word_list(patent.abstract)
    patent.abstract = _stem_words_list(patent.abstract)
    # TO-DO: Implement title retrieval
    #    patent.title = _extract_word_list(patent.title)
    #    patent.title = _stem_words_list(patent.title)
    return patent

def get_term_document_matrix(vectorizer, iterable_documents):
    """Get a document-term matrix from an iterable that yields strings

    :param vectorizer: An Sklearn CountVectorizer object with an attached vocabulary
    :param iterable_documents: The iterable that yields strings
    :rtype: An array of size [n_samples, n_features]
    """
    matrix = vectorizer.fit_transform(iterable_documents)
    return matrix

def normalize_matrix(transformer, matrix):
    """Normalize count matrix to scale down the impact of very frequent tokens

    :param transformer: A Sklearn TfidfTransformer object
    :param matrix: An array representing a term document matrix,
    output of CountVectorizer.fit_transform
    """
    matrix_normalized = transformer.fit_transform(matrix)
    return matrix_normalized
