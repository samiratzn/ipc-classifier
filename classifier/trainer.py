"""
"""
from classifier import preprocessing
from sklearn.naive_bayes import MultinomialNB

def train_section_classifier(vectorizer_count, tfidftransformer, patents):
    vectors_features_tfidf = preprocessing.get_tfidf_features(vectorizer_count,
                                                              tfidftransformer,
                                                              patents)
    sections = []
    for patent in patents:
        sections.append(patent.ipcs[0])
    classifier_sections = MultinomialNB()
    classifier_sections.fit(vectors_features_tfidf, sections)
    return (classifier_sections, sections)

def _filter_patents(sections, patents):
    patents_filtered = [patent for patent in patents if patent.ipcs[0] in sections]
    return patents_filtered

def train_class_classifier(vectorizer_count, tfidftransformer, sections, patents):
    patents_filtered = _filter_patents(sections, patents)
    vectors_features_tfidf = preprocessing.get_tfidf_features(vectorizer_count,
                                                              tfidftransformer,
                                                              patents_filtered)
    classes = []
    for patent in patents_filtered:
        classes.append(patent.ipcs[:3])
    classifier_classes = MultinomialNB()
    classifier_classes.fit(vectors_features_tfidf, classes)
    return classifier_classes
