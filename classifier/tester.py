"""
"""
from classifier import preprocessing

def get_top_3(predictions):
    top_3 = sorted(predictions, reverse=True)[:3]
    return top_3

def map_top_3(top_3_probs, prediction):
    top_3_indexes = []
    for i, prob in enumerate(prediction):
        if prob in top_3_probs:
            top_3_indexes.append(i)
    return top_3_indexes

def predict_top_3_sections(vectorizer_count, tfidftransformer, classifier, patents):
    vector_features_tf = preprocessing.get_tfidf_features_test(vectorizer_count,
                                                               tfidftransformer,
                                                               patents)
    predictions = classifier.predict_proba(vector_features_tf)
    list_top_3_indexes = []
    for prediction in predictions:
        top_3_probs = get_top_3(prediction)
        top_3_indexes = map_top_3(top_3_probs, prediction)
        list_top_3_indexes.append(top_3_indexes)
    return list_top_3_indexes

def predict_top_3_classes(vectorizer_count, tfidftransformer, classifier, patent):
    vector_features_tf = preprocessing.get_tfidf_features_test(vectorizer_count,
                                                               tfidftransformer,
                                                               list(patent))
    predictions = classifier.predict_proba(vector_features_tf)
    top_3_probs = get_top_3(predictions)
    top_3_indexes = map_top_3(top_3_probs, predictions)
    return top_3_indexes
