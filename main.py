"""
"""
from sklearn import feature_extraction
from classifier import preprocessing
from classifier import trainer
from classifier import tester

def main(path_data):
    text_train_index = preprocessing.source_index(path_data, '/train')
    patents_train = preprocessing.get_patents(text_train_index)
    vectorizer_count = feature_extraction.text.CountVectorizer(input='content',
                                                               encoding='ISO-8859-1')
    tfidftransformer = feature_extraction.text.TfidfTransformer(norm='l2')
    classifier_sections, sections = trainer.train_section_classifier(vectorizer_count,
                                                                     tfidftransformer,
                                                                     patents_train)

    text_test_index = preprocessing.source_index(path_data, '/test')
    patents_test = preprocessing.get_patents(text_test_index)
    predictions_top_3_indexes = tester.predict_top_3_sections(vectorizer_count,
                                                              tfidftransformer,
                                                              classifier_sections,
                                                              patents_test)
    for prediction in predictions_top_3_indexes:
        for index in prediction:
            print(sections[index])
    #predictions_top_3_classes = []
    #for prediction_sections in predictions_top_3_sections:
    #    vectorizer_count_class = feature_extraction.text.CountVectorizer(input='content',
    #                                                                     encoding='ISO-8859-1')
    #    tfidftransformer_class = feature_extraction.text.TfidfTransformer()
    #    classifier_classes = trainer.train_class_classifier(vectorizer_count_class,
    #                                                        tfidftransformer_class,
    #                                                        prediction_sections,
    #                                                        patents_test)
    #    for patent in patents_test:
    #        predictions_top_3_classes.append(
    #            tester.predict_top_3_classes(vectorizer_count_class,
    #                                         tfidftransformer_class,
    #                                         classifier_classes,
    #                                         patent)
    #        )
    #
    #for patent in enumerate(predictions_top_3_classes):
    #    print("{} ".format(patent))

if __name__ == '__main__':
    main('wipo-alpha')
