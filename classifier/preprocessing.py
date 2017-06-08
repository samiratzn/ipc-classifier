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

def preprocess_training_data(path_data):
    """Manipulate the data to have a proper representation for the model to consume

    :param path_training_data: A string, is the relative path to the training data root
    directory. It should not have a trailing `/`.
    """
    path_index = path_data + '/index_training.txt'
    path_training_data = path_data + '/train'
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

    patents = []
    for path_document in text_index.split('\n'):
        with open(path_document, 'r', encoding='ISO-8859-1') as file_document:
            print('Loading {} to memory.'.format(path_document))
            text_document = file_document.read()
            patent = utils.get_patent(text_document)
            patent_transformed = utils.transform_patent(patent)
            patents.append(patent_transformed)
    print('Done.')

    count_vectorizer = sklearn.feature_extraction.text.CountVectorizer(input='content',
                                                                       encoding='ISO-8859-1')
    tfidftransformer = sklearn.feature_extraction.text.TfidfTransformer()
    iterator_patent_text = (' '.join(patent.title.union(patent.abstract)) for patent in patents)
    vectors_features_tf = utils.get_term_document_matrix(count_vectorizer,
                                                         iterator_patent_text)
    vectors_features_tfidf = utils.normalize_matrix(tfidftransformer, vectors_features_tf)
    return vectors_features_tfidf
