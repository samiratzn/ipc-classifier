"""Text preprocessing module"""
import os
import sklearn
from classifier import preprocessing_tools as utils

def create_index(path_data):
    """Use os.walk to create an index for a directory
    """
    entries_index = []
    for root, dirs, files in os.walk(path_data):
        for item in files:
            entries_index.append(os.path.join(root, item))
    return '\n'.join(entries_index[2:])

def get_patents(text_index):
    patents = []
    print('Loading documents.')
    for path_document in text_index.split('\n'):
        with open(path_document, 'r', encoding='ISO-8859-1') as file_document:
            #print('Loading {} to memory.'.format(path_document))
            text_document = file_document.read()
            patent = utils.get_patent(text_document)
            patent_transformed = utils.transform_patent(patent)
            patents.append(patent_transformed)
    print('Done.')
    return patents

def get_patent_text_iterator(patents):
    iterator_patent_text = (' '.join(patent.title.union(patent.abstract)) for patent in patents)
    return iterator_patent_text

def source_index(path_data, path_sub):
    path_index = path_data + '/index_' + path_sub[1:]
    path_training_data = path_data + path_sub
    if not os.path.isfile(path_index):
        print('Creating index, please wait.')
        text_index = create_index(path_training_data)
        with open(path_index, 'w') as file_index:
            file_index.write(text_index)
            print('Done.')
    else:
        print('Reading index.')
        with open(path_index, 'r') as file_index:
            text_index = file_index.read()
            print('Done.')
    return text_index

def get_features_count(vectorizer_count, patents):
    iterator_patent_text = get_patent_text_iterator(patents)
    vectors_features_count = utils.get_term_document_matrix(vectorizer_count,
                                                            iterator_patent_text)
    return vectors_features_count

def get_features_count_test(vectorizer_count, patents):
    iterator_patent_text = get_patent_text_iterator(patents)
    vectors_features_count = utils.get_term_document_matrix_test(vectorizer_count,
                                                                 iterator_patent_text)
    return vectors_features_count

def get_tfidf_features(vectorizer_count, tfidftransformer, patents):
    """Manipulate the data to have a proper representation for the model to consume

    :param path_training_data: A string, is the relative path to the training data root
    directory. It should not have a trailing `/`.
    """
    vectors_count = get_features_count(vectorizer_count, patents)
    vectors_features_tfidf = utils.get_tfidf_matrix(tfidftransformer, vectors_count)
    return vectors_features_tfidf

def get_tfidf_features_test(vectorizer_count, tfidftransformer, patents):
    """Manipulate the data to have a proper representation for the model to consume

    :param path_training_data: A string, is the relative path to the training data root
    directory. It should not have a trailing `/`.
    """
    vectors_count = get_features_count_test(vectorizer_count, patents)
    vectors_features_tfidf = utils.get_tfidf_matrix(tfidftransformer, vectors_count)
    return vectors_features_tfidf
